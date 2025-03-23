class Assign:
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr

class Print:
    def __init__(self, expr):
        self.expr = expr

class If:
    def __init__(self, cond, then, else_):
        self.cond = cond
        self.then = then
        self.else_ = else_

class While:
    def __init__(self, cond, body):
        self.cond = cond
        self.body = body

class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num:
    def __init__(self, value):
        self.value = value

class Var:
    def __init__(self, name):
        self.name = name
