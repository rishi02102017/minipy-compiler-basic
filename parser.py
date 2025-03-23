import ply.yacc as yacc
from lexer import tokens
import minipy_ast as custom_ast  


def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : assignment
                 | print_stmt
                 | if_stmt
                 | while_stmt'''
    p[0] = p[1]

def p_assignment(p):
    'assignment : ID ASSIGN expression'
    p[0] = custom_ast.Assign(p[1], p[3])

def p_print_stmt(p):
    'print_stmt : PRINT LPAREN expression RPAREN'
    p[0] = custom_ast.Print(p[3])

def p_if_stmt(p):
    'if_stmt : IF expression statement_list ELSE statement_list'
    p[0] = custom_ast.If(p[2], p[3], p[5])

def p_while_stmt(p):
    'while_stmt : WHILE expression statement_list'
    p[0] = custom_ast.While(p[2], p[3])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MUL expression
                  | expression DIV expression
                  | expression LT expression'''
    p[0] = custom_ast.BinOp(p[1], p[2], p[3])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = custom_ast.Num(p[1])

def p_expression_id(p):
    'expression : ID'
    p[0] = custom_ast.Var(p[1])

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()
