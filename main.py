from lexer import lexer
from parser import parser
from codegen import generate

if __name__ == "__main__":
    code = open("examples/test.minipy").read()
    ast = parser.parse(code, lexer=lexer)
    bytecode = generate(ast)
    for line in bytecode:
        print(line)
