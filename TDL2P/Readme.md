# Readme.md

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
