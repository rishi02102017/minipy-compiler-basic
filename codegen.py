import minipy_ast as custom_ast  

def generate(node):
    bytecode = []

    def walk(n):
        if isinstance(n, list):
            for stmt in n:
                walk(stmt)
        elif isinstance(n, custom_ast.Assign):
            walk(n.expr)
            bytecode.append(f'STORE {n.var}')
        elif isinstance(n, custom_ast.Print):
            walk(n.expr)
            bytecode.append('PRINT')
        elif isinstance(n, custom_ast.BinOp):
            walk(n.left)
            walk(n.right)
            bytecode.append(f'{n.op.upper()}')
        elif isinstance(n, custom_ast.Num):
            bytecode.append(f'PUSH {n.value}')
        elif isinstance(n, custom_ast.Var):
            bytecode.append(f'LOAD {n.name}')
        elif isinstance(n, custom_ast.If):
            walk(n.cond)
            bytecode.append('JZ else')
            walk(n.then)
            bytecode.append('JMP end')
            bytecode.append('else:')
            walk(n.else_)
            bytecode.append('end:')
        elif isinstance(n, custom_ast.While):
            bytecode.append('loop:')
            walk(n.cond)
            bytecode.append('JZ endloop')
            walk(n.body)
            bytecode.append('JMP loop')
            bytecode.append('endloop:')

    walk(node)
    return bytecode
