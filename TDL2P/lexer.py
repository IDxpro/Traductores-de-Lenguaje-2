from ply import lex

# Definición de tokens
tokens = (
    'ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN',
    'SEMICOLON', 'ASSIGN', 'PRINT', 'INT', 'RETURN', 'LBRACES', 'RBRACES'
)

# Reglas de expresiones regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACES = r'\{'
t_RBRACES = r'\}'
t_SEMICOLON = r';'
t_ASSIGN = r'='
t_PRINT = r'printf'
t_ignore = ' \t'
t_INT = r'int'
t_RETURN = r'return'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value == 'int' or t.value == 'float':
        t.type = t.value.upper()  # Palabras clave
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()

class LexerWrapper:
    def __init__(self, code):
        self.lexer = lexer
        self.lexer.input(code)
        self.tokens = []

        # Store all tokens
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            self.tokens.append(tok)

    def get_tokens(self):
        return self.tokens
