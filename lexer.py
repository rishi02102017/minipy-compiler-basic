import ply.lex as lex

# Tokens
tokens = ['NUMBER', 'ID', 'PLUS', 'MINUS', 'MUL', 'DIV',
          'ASSIGN', 'LPAREN', 'RPAREN', 'LT',
          'IF', 'ELSE', 'WHILE', 'PRINT']

# Token regex rules
t_PLUS = r'\+'
t_MINUS = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LT = r'<'

# Reserved keywords
reserved = {'if': 'IF', 'else': 'ELSE', 'while': 'WHILE', 'print': 'PRINT'}

# Identifier / Keyword
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignore spaces, tabs
t_ignore = ' \t'

# Ignore colons
def t_ignore_colon(t):
    r':'
    pass

# Ignore comments
def t_comment(t):
    r'\#.*'
    pass

# Line numbers (optional, helps with debugging)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling
def t_error(t):
    print(f"Illegal char: {repr(t.value[0])}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
