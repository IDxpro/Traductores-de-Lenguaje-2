# Assembler

Este código en Python implementa un compilador básico que realiza el análisis léxico, sintáctico y semántico de un programa en lenguaje C y genera código ensamblador equivalente. A continuación, se explica el código por partes:

## Importación de módulos

```python
import c_to_assembly
import semantic
import sintax
import lexer as lex_module
```

Aquí se importan los módulos necesarios para el compilador, incluyendo `c_to_assembly` para la generación de código ensamblador, `semantic` para el análisis semántico, `sintax` para el análisis sintáctico y `lexer` para el análisis léxico.

## Clase Lexer

```python
class Lexer:
    def __init__(self, code):
        self.lexer_wrapper = lex_module.LexerWrapper(code)
        self.tokens = self.lexer_wrapper.get_tokens()
```

La clase `Lexer` se encarga de realizar el análisis léxico del código fuente. Toma el código fuente como entrada y genera una lista de tokens utilizando el módulo `lexer`.

## Clase Parser

```python
class Parser:
    def __init__(self, tokens):
        self.parser = sintax.Parser(tokens)

    def parse(self):
        result = self.parser.parse_program()
        print("Parsing completed")
        return result
```

La clase `Parser` se encarga del análisis sintáctico del programa. Utiliza la lista de tokens generada por el `Lexer` para construir un árbol de sintaxis abstracta (AST) utilizando el módulo `sintax`.

## Clase SemanticAnalyzer

```python
class SemanticAnalyzer:
    def __init__(self, parser):
        self.parser = parser

    def analyze(self):
        semantic.analizador_semantico(self.parser)
```

La clase `SemanticAnalyzer` realiza el análisis semántico del programa utilizando el módulo `semantic` y el árbol de sintaxis abstracta generado por el `Parser`.

## Clases IntermediateCodeGenerator, Optimizer y CodeGenerator (comentadas)

```python
"""
class IntermediateCodeGenerator:
    def __init__(self, parser):
        self.parser = parser
        self.intermediate_code = []

    def generate_code(self):
        self.intermediate_code = c_to_assembly.generate_intermediate_code(self.parser)

class Optimizer:
    def __init__(self, intermediate_code):
        self.intermediate_code = intermediate_code

    def optimize(self):
        self.intermediate_code = c_to_assembly.optimize_code(self.intermediate_code)

class CodeGenerator:
    def __init__(self, intermediate_code):
        self.intermediate_code = intermediate_code
        self.machine_code = []

    def generate_machine_code(self):
        self.machine_code = c_to_assembly.generate_machine_code(self.intermediate_code)
        return self.machine_code
"""
```

Estas clases están comentadas en el código proporcionado, pero representan las etapas de generación de código intermedio, optimización y generación de código máquina. Estas etapas no se implementan en el código actual.

## Uso del compilador

```python
source_code = """
int main() {
    int a = 10;
    int b = 20;
    int c = a - b;
    return = 0;
}
"""

source_code_python = """
def main():
    a = 10
    b = 20
    c = a - b
    return 0
"""

lexer = Lexer(source_code)
parser = Parser(lexer.tokens)
semantic_analyzer = SemanticAnalyzer(source_code)

c_code = c_to_assembly.translate_to_assembler(source_code)

# Ejecutar el compilador
parser.parse()
semantic_analyzer.analyze()

print(c_code)
print(semantic.creador_ast(source_code_python))
```

En esta sección, se define el código fuente en lenguaje C (`source_code`) y una versión en Python (`source_code_python`).

Se crea una instancia de la clase `Lexer` con el código fuente en C y se obtienen los tokens. Luego, se crea una instancia de la clase `Parser` con los tokens y se crea una instancia de la clase `SemanticAnalyzer` con el código fuente en C.

Se llama a la función `translate_to_assembler` del módulo `c_to_assembly` para generar el código ensamblador equivalente al código fuente en C.

Finalmente, se ejecutan las etapas de análisis sintáctico y semántico utilizando los métodos `parse()` y `analyze()` de las clases `Parser` y `SemanticAnalyzer`, respectivamente.

Se imprime el código ensamblador generado (`c_code`) y el árbol de sintaxis abstracta (AST) generado a partir del código fuente en Python (`semantic.creador_ast(source_code_python)`).

En resumen, este código implementa un compilador básico que realiza el análisis léxico, sintáctico y semántico de un programa en lenguaje C y genera código ensamblador equivalente. Además, muestra cómo utilizar los módulos del compilador y cómo generar un árbol de sintaxis abstracta a partir de código Python.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Lexer.py

Este archivo contiene la implementación de un lexer (analizador léxico) utilizando la biblioteca PLY (Python Lex-Yacc) en Python. El lexer se encarga de dividir el código fuente en tokens (palabras clave, identificadores, números, operadores, etc.) para su posterior análisis sintáctico y semántico.

## Definición de tokens

```python
tokens = (
    'ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN',
    'SEMICOLON', 'ASSIGN', 'PRINT', 'INT', 'RETURN', 'LBRACES', 'RBRACES'
)
```

Aquí se definen los tokens que el lexer debe reconocer. Estos incluyen identificadores (`ID`), números (`NUMBER`), operadores aritméticos (`PLUS`, `MINUS`, `TIMES`, `DIVIDE`), paréntesis (`LPAREN`, `RPAREN`), punto y coma (`SEMICOLON`), operador de asignación (`ASSIGN`), la palabra clave `printf` (`PRINT`), la palabra clave `int` (`INT`), la palabra clave `return` (`RETURN`), y llaves para bloques de código (`LBRACES`, `RBRACES`).

## Reglas de expresiones regulares para tokens simples

```python
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
```

Estas reglas definen las expresiones regulares que se utilizarán para reconocer los tokens simples, como operadores, paréntesis, llaves, punto y coma, operador de asignación y palabras clave.

## Reglas para identificadores y números

```python
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value == 'int' or t.value == 'float':
        t.type = t.value.upper()  # Palabras clave
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
```

Estas funciones definen las reglas para reconocer identificadores (`t_ID`) y números enteros (`t_NUMBER`).

- `t_ID` reconoce cadenas que comienzan con una letra o guión bajo, seguidas de letras, dígitos o guiones bajos. Si la cadena coincide con las palabras clave `int` o `float`, se establece el tipo de token correspondiente en mayúsculas.
- `t_NUMBER` reconoce cadenas de dígitos y convierte su valor a un número entero.

## Regla para saltos de línea

```python
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
```

Esta función define la regla para reconocer saltos de línea (`\n`). Cuando se encuentra un salto de línea, se incrementa el contador de líneas del lexer (`t.lexer.lineno`).

## Manejo de errores

```python
def t_error(t):
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)
```

Esta función se llama cuando el lexer encuentra un carácter que no coincide con ninguna de las reglas definidas. En este caso, se imprime un mensaje de error indicando el carácter ilegal y se omite ese carácter en el análisis léxico.

## Construcción del lexer

```python
lexer = lex.lex()
```

Esta línea construye el lexer utilizando las reglas y tokens definidos anteriormente.

## Clase LexerWrapper

```python
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
```

La clase `LexerWrapper` proporciona una interfaz más cómoda para utilizar el lexer. Toma el código fuente como entrada y genera una lista de tokens utilizando el lexer construido anteriormente. La función `get_tokens()` devuelve la lista de tokens generada.

En resumen, este archivo contiene la implementación de un lexer que reconoce tokens básicos para un lenguaje de programación simple. El lexer se construye utilizando la biblioteca PLY y se proporciona una clase `LexerWrapper` para facilitar su uso.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Syntax

This code implements a recursive descent parser for a simple programming language using Python. The parser takes a list of tokens as input and builds an abstract syntax tree (AST) by recognizing valid syntactic structures and performing corresponding actions.

## Parser Class

```python
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        self.current_token = self.tokens[self.current_token_index]
        print(f"Initial token: {self.current_token}")
```

The `Parser` class is initialized with a list of tokens obtained from the lexer. It keeps track of the current token index and the current token being processed. The initial token is printed for debugging purposes.

### Helper Methods

```python
def error(self, message="Invalid syntax"):
    raise Exception(message)

def eat(self, token_type):
    print(f"Eating token: {self.current_token}, expected: {token_type}")
    if self.current_token.type == token_type:
        self.current_token_index += 1
        if self.current_token_index < len(self.tokens):
            self.current_token = self.tokens[self.current_token_index]
            print(f"Next token: {self.current_token}")
        else:
            self.current_token = None
    else:
        self.error(f"Expected token type {token_type}, got {self.current_token.type}")
```

The `error` method raises an exception with a custom error message.

The `eat` method consumes the current token if its type matches the expected token type. It also updates the `current_token` and `current_token_index` accordingly. If the current token type does not match the expected type, an error is raised.

### Parsing Methods

```python
def parse_function(self):
    print("Parsing function")
    self.eat("INT")  # Assuming return type is int
    self.eat("ID")
    self.eat("LPAREN")
    self.eat("RPAREN")
    self.eat("LBRACES")
    while self.current_token and self.current_token.type != "RBRACES":
        self.parse_statement()
    self.eat("RBRACES")

def parse_statement(self):
    print(f"Parsing statement: {self.current_token}")
    if self.current_token.type == "INT":
        self.eat("INT")
        self.eat("ID")
        if self.current_token.type == "ASSIGN":
            self.eat("ASSIGN")
            self.parse_expression()
        self.eat("SEMICOLON")
    elif self.current_token.type == "ID":
        self.eat("ID")
        self.eat("ASSIGN")
        self.parse_expression()
        self.eat("SEMICOLON")
    elif self.current_token.type == "RETURN":
        self.eat("RETURN")
        self.parse_expression()
        self.eat("SEMICOLON")
    else:
        self.error("Invalid statement")

def parse_expression(self):
    print(f"Parsing expression: {self.current_token}")
    if self.current_token.type == "ID":
        self.eat("ID")
    elif self.current_token.type == "NUMBER":
        self.eat("NUMBER")
    else:
        self.error("Invalid expression")

    while self.current_token and self.current_token.type in {"PLUS", "MINUS"}:
        self.eat(self.current_token.type)
        if self.current_token.type == "ID":
            self.eat("ID")
        elif self.current_token.type == "NUMBER":
            self.eat("NUMBER")
        else:
            self.error("Invalid expression after operator")
```

The `parse_function` method parses a function declaration by consuming the return type (`INT`), identifier (`ID`), parentheses (`LPAREN` and `RPAREN`), and braces (`LBRACES` and `RBRACES`). It calls `parse_statement` repeatedly to parse the statements inside the function.

The `parse_statement` method parses a statement, which can be a variable declaration, assignment, or return statement. Depending on the current token type, it calls the appropriate parsing methods and consumes the necessary tokens.

The `parse_expression` method parses an expression, which can be an identifier (`ID`) or a number (`NUMBER`). It also handles binary operators (`PLUS` and `MINUS`) by consuming the operator and the subsequent operand.

```python
def parse_program(self):
    print("Parsing program")
    while self.current_token:
        print(f"Current token in parse_program: {self.current_token}")
        if self.current_token.type == "INT":
            self.parse_function()
        else:
            self.error("Program must start with a function")
    return True
```

The `parse_program` method is the entry point for parsing the entire program. It iterates over the tokens and calls `parse_function` if the current token type is `INT` (assuming that the program starts with a function declaration). If the current token type is not `INT`, an error is raised.

The parser uses a recursive descent approach, where each parsing method handles a specific syntactic structure (e.g., function, statement, expression) and calls other parsing methods as needed. The `eat` method is used to consume tokens and advance the parsing process.

Note that this is a simplified implementation and may not handle all possible syntactic structures or error cases. It should be extended and modified to accommodate the specific requirements of the programming language being parsed.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# c_to_assembly.py

This code provides a function `translate_to_assembler` that takes C code as input and generates equivalent assembly code for the x86 architecture. It also includes placeholder functions for generating intermediate code, optimizing code, and generating machine code, although their implementations are not provided.

## `translate_to_assembler` Function

```python
def translate_to_assembler(c_code):
    assembly_code = []
    c_to_assembler = {
        'int': '',  # 'int' keyword will be handled separately
        '+': 'add',
        '-': 'sub',
        '*': 'mul',
        '/': 'div',
        '=': 'mov',
        'return': 'mov eax,',
        'printf': 'call printf',
        'scanf': 'call scanf'
        # Add more mappings as needed
    }
    lines = c_code.strip().split('\n')
    variable_declarations = {}
    label_counter = 0

    for line in lines:
        line = line.strip().strip(';')
        if not line:
            continue
        tokens = line.split()

        # Handle main function
        if line.startswith('int main'):
            assembly_code.append('section .text')
            assembly_code.append('global main')
            assembly_code.append('main:')

        # Handle variable declarations
        elif tokens[0] == 'int':
            var_name = tokens[1]
            if len(tokens) > 3 and tokens[2] == '=':
                var_value = tokens[3]
                assembly_code.append(f'mov dword [{var_name}], {var_value}')
            else:
                assembly_code.append(f'mov dword [{var_name}], 0')
            variable_declarations[var_name] = 0

        # Handle arithmetic operations
        elif '=' in tokens:
            dest = tokens[0]
            src = tokens[2:]
            if len(src) == 1:
                src = src[0]
                assembly_code.append(f'mov eax, {src}')
                assembly_code.append(f'mov [{dest}], eax')
            else:
                operand1 = src[0]
                operator = src[1]
                operand2 = src[2]
                assembly_code.append(f'mov eax, {operand1}')
                assembly_code.append(f'{c_to_assembler[operator]} eax, {operand2}')
                assembly_code.append(f'mov [{dest}], eax')

        # Handle return statement
        elif tokens[0] == 'return':
            ret_value = tokens[1]
            assembly_code.append(f'mov eax, {ret_value}')
            assembly_code.append('ret')

    return '\n'.join(assembly_code)
```

The `translate_to_assembler` function takes C code as input and generates equivalent assembly code for the x86 architecture. Here's how it works:

1. The function initializes an empty list `assembly_code` to store the generated assembly code.
2. It defines a dictionary `c_to_assembler` that maps C operators and keywords to their respective assembly instructions.
3. The C code is split into lines, and each line is processed individually.
4. If the line starts with `'int main'`, it generates the necessary assembly code for the `main` function.
5. If the line contains a variable declaration (`'int'`), it generates assembly code to initialize the variable with a value or set it to zero.
6. If the line contains an arithmetic operation (`'='`), it generates assembly code to perform the operation using the appropriate instructions from `c_to_assembler`.
7. If the line contains a `'return'` statement, it generates assembly code to move the return value into the `eax` register and return from the function.
8. Finally, the function returns the generated assembly code as a string, with lines separated by newline characters.

## Placeholder Functions

```python
def generate_intermediate_code(parser):
    # Generate intermediate code from the parser
    intermediate_code = []
    # Implementation here
    return intermediate_code

def optimize_code(intermediate_code):
    # Optimize the intermediate code
    optimized_code = intermediate_code
    # Implementation here
    return optimized_code

def generate_machine_code(intermediate_code):
    # Generate machine code from the intermediate code
    machine_code = []
    # Implementation here
    return machine_code
```

These functions are placeholders for generating intermediate code, optimizing code, and generating machine code, respectively. Their implementations are not provided in the given code.

## Example Usage

```python
# Example usage:
c_code = """
int main() {
    int a = 10;
    int b = 20;
    int c = a + b;
    return 0;
}
"""

assembly_code = translate_to_assembler(c_code)
print(assembly_code)
```

This code block demonstrates how to use the `translate_to_assembler` function. It defines a C code snippet, calls the `translate_to_assembler` function with the C code, and prints the generated assembly code.

In summary, this code provides a basic implementation for translating C code to assembly code for the x86 architecture, with placeholders for generating intermediate code, optimizing code, and generating machine code. It can be extended and improved to handle more complex C constructs and generate optimized machine code.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# semantic.py

Este código en Python proporciona dos funciones: `analizador_semantico` y `creador_ast`. La función `analizador_semantico` realiza un análisis semántico básico de un código fuente en Python, mientras que la función `creador_ast` genera y imprime el árbol de sintaxis abstracta (AST) del código fuente.

## Función `analizador_semantico`

```python
def analizador_semantico(codigo):
    # Expresión regular para detectar declaraciones de variables y asignaciones
    patron_declaracion = r'(\w+)\s+(\w+)\s*;'
    patron_asignacion = r'(\w+)\s*=\s*(\w+)\s*(\[+\-*/\])\s*(\w+)\s*;'

    # Buscar coincidencias de declaraciones y asignaciones
    coincidencias_declaracion = re.findall(patron_declaracion, codigo)
    coincidencias_asignacion = re.findall(patron_asignacion, codigo)

    # Analizar las declaraciones
    for tipo, variable in coincidencias_declaracion:
        print(f"Se encontró una declaración de variable: Tipo: {tipo}, Variable: {variable}")

    # Analizar las asignaciones
    for var_destino, var1, operador, var2 in coincidencias_asignacion:
        print(f"Se encontró una asignación: {var_destino} = {var1} {operador} {var2}")
```

La función `analizador_semantico` toma el código fuente como entrada y realiza un análisis semántico básico utilizando expresiones regulares. Utiliza dos patrones de expresiones regulares: `patron_declaracion` para detectar declaraciones de variables, y `patron_asignacion` para detectar asignaciones.

Luego, busca todas las coincidencias de estos patrones en el código fuente utilizando `re.findall`. Para cada coincidencia de declaración, imprime un mensaje indicando el tipo y el nombre de la variable. Para cada coincidencia de asignación, imprime un mensaje indicando la variable de destino, las variables operandos y el operador utilizado.

## Función `creador_ast`

```python
def creador_ast(codigo):
    # Parsear el código en un AST
    tree = ast.parse(codigo)

    # Función para imprimir el AST de manera estilizada
    def pprint_ast(node, indent=0, is_leaf=False):
        if isinstance(node, ast.AST):
            print(' ' * indent + f"Nodo: {type(node).__name__}")
            for child_node in ast.iter_child_nodes(node):
                pprint_ast(child_node, indent + 4)
        else:
            print(' ' * indent + f"Hoja: {node}")

    # Imprimir el AST estilizado
    pprint_ast(tree)
```

La función `creador_ast` toma el código fuente como entrada y genera el árbol de sintaxis abstracta (AST) utilizando el módulo `ast` de Python. Luego, utiliza una función auxiliar `pprint_ast` para imprimir el AST de manera estilizada.

La función `pprint_ast` es una función recursiva que imprime los nodos del AST con su tipo y sus nodos hijos. Si un nodo es una hoja (no tiene nodos hijos), se imprime su valor. La sangría se utiliza para mostrar la estructura jerárquica del árbol.

## Uso de las funciones

```python
# Código de ejemplo
codigo_c = """
def main():
    a = 10
    b = 20
    c = a - b
    return 0
"""

analizador_semantico(codigo_c)
creador_ast(codigo_c)
```

En esta parte del código, se define un ejemplo de código fuente en Python (`codigo_c`). Luego, se llama a la función `analizador_semantico` con este código, lo que imprimirá los mensajes correspondientes al análisis semántico. Después, se llama a la función `creador_ast` con el mismo código, lo que imprimirá el árbol de sintaxis abstracta (AST) generado.

En resumen, este código proporciona dos funciones útiles: `analizador_semantico` para realizar un análisis semántico básico utilizando expresiones regulares, y `creador_ast` para generar y imprimir el árbol de sintaxis abstracta de un código fuente en Python.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Expected Output

```python
Connected to Python 3.11.9


Nodo: Module
Initial token: LexToken(INT,'int',2,1)
Parsing program
Current token in parse_program: LexToken(INT,'int',2,1)
Parsing function
Eating token: LexToken(INT,'int',2,1), expected: INT
Next token: LexToken(ID,'main',2,5)
Eating token: LexToken(ID,'main',2,5), expected: ID
Next token: LexToken(LPAREN,'(',2,9)
Eating token: LexToken(LPAREN,'(',2,9), expected: LPAREN
Next token: LexToken(RPAREN,')',2,10)
Eating token: LexToken(RPAREN,')',2,10), expected: RPAREN
Next token: LexToken(LBRACES,'{',2,12)
Eating token: LexToken(LBRACES,'{',2,12), expected: LBRACES
Next token: LexToken(INT,'int',3,18)
Parsing statement: LexToken(INT,'int',3,18)
Eating token: LexToken(INT,'int',3,18), expected: INT
Next token: LexToken(ID,'a',3,22)
Eating token: LexToken(ID,'a',3,22), expected: ID
Next token: LexToken(ASSIGN,'=',3,24)
Eating token: LexToken(ASSIGN,'=',3,24), expected: ASSIGN
Next token: LexToken(NUMBER,10,3,26)
Parsing expression: LexToken(NUMBER,10,3,26)
Eating token: LexToken(NUMBER,10,3,26), expected: NUMBER
Next token: LexToken(SEMICOLON,';',3,28)
Eating token: LexToken(SEMICOLON,';',3,28), expected: SEMICOLON
Next token: LexToken(INT,'int',4,34)
Parsing statement: LexToken(INT,'int',4,34)
Eating token: LexToken(INT,'int',4,34), expected: INT
Next token: LexToken(ID,'b',4,38)
Eating token: LexToken(ID,'b',4,38), expected: ID
Next token: LexToken(ASSIGN,'=',4,40)
Eating token: LexToken(ASSIGN,'=',4,40), expected: ASSIGN
Next token: LexToken(NUMBER,20,4,42)
Parsing expression: LexToken(NUMBER,20,4,42)
Eating token: LexToken(NUMBER,20,4,42), expected: NUMBER
Next token: LexToken(SEMICOLON,';',4,44)
Eating token: LexToken(SEMICOLON,';',4,44), expected: SEMICOLON
Next token: LexToken(INT,'int',5,50)
Parsing statement: LexToken(INT,'int',5,50)
Eating token: LexToken(INT,'int',5,50), expected: INT
Next token: LexToken(ID,'c',5,54)
Eating token: LexToken(ID,'c',5,54), expected: ID
Next token: LexToken(ASSIGN,'=',5,56)
Eating token: LexToken(ASSIGN,'=',5,56), expected: ASSIGN
Next token: LexToken(ID,'a',5,58)
Parsing expression: LexToken(ID,'a',5,58)
Eating token: LexToken(ID,'a',5,58), expected: ID
Next token: LexToken(MINUS,'-',5,60)
Eating token: LexToken(MINUS,'-',5,60), expected: MINUS
Next token: LexToken(ID,'b',5,62)
Eating token: LexToken(ID,'b',5,62), expected: ID
Next token: LexToken(SEMICOLON,';',5,63)
Eating token: LexToken(SEMICOLON,';',5,63), expected: SEMICOLON
Next token: LexToken(ID,'return',6,69)
Parsing statement: LexToken(ID,'return',6,69)
Eating token: LexToken(ID,'return',6,69), expected: ID
Next token: LexToken(ASSIGN,'=',6,76)
Eating token: LexToken(ASSIGN,'=',6,76), expected: ASSIGN
Next token: LexToken(NUMBER,0,6,78)
Parsing expression: LexToken(NUMBER,0,6,78)
Eating token: LexToken(NUMBER,0,6,78), expected: NUMBER
Next token: LexToken(SEMICOLON,';',6,79)
Eating token: LexToken(SEMICOLON,';',6,79), expected: SEMICOLON
Next token: LexToken(RBRACES,'}',7,81)
Eating token: LexToken(RBRACES,'}',7,81), expected: RBRACES
Parsing completed
Se encontró una asignación: c = a - b
section .text
global main
main:
mov dword [a], 10
mov dword [b], 20
mov dword [c], a
mov eax, 0
mov [return], eax
Nodo: Module
    Nodo: FunctionDef
        Nodo: arguments
        Nodo: Assign
            Nodo: Name
                Nodo: Store
            Nodo: Constant
        Nodo: Assign
            Nodo: Name
                Nodo: Store
            Nodo: Constant
        Nodo: Assign
            Nodo: Name
                Nodo: Store
            Nodo: BinOp
                Nodo: Name
                    Nodo: Load
                Nodo: Sub
                Nodo: Name
                    Nodo: Load
        Nodo: Return
            Nodo: Constant
None
```

