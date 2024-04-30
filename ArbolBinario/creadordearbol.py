from ply import lex, yacc

# Definición de tokens
tokens = (
    'INT', 'FLOAT', 'ID', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN',
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \t\n'

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_error(t):
    print(f"Error léxico: Carácter '{t.value[0]}' no válido")
    t.lexer.skip(1)

lexer = lex.lex()

# Definición de la gramática
def p_statement_expression(p):
    '''statement : expression'''
    p[0] = p[1]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_number(p):
    '''expression : INT
                  | FLOAT'''
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    p[0] = ('ID', p[1])

def p_error(p):
    print("Error sintáctico:", p)

parser = yacc.yacc()

# Ejemplo de uso
if __name__ == '__main__':
    data = '''
    float a;
    int b;
    int c;
    c = a + b;
    c = suma(8, 9);
    '''
    lexer.input(data)
    for tok in lexer:
        print(tok)

    result = parser.parse(data)
    print(result)
