from ply import lex, yacc
import re
import c_to_assembly
import lexer as lex_module
import semantic
import sintax
import test

class Lexer:
    def __init__(self, code):
        self.code = code
        self.lexer = lex_module.Lexer(code)

    def get_next_token(self):
        return self.lexer.get_next_token()

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
        print(f"Initial token: {self.current_token}")

    def parse(self):
        result = sintax.Parser(self.lexer).parse_program()
        print("Parsing completed")
        return result

class SemanticAnalyzer:
    def __init__(self, parser):
        self.parser = parser

    def analyze(self):
        semantic.analizador_semantico(self.parser)

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

# Uso del compilador
source_code = """
int main() {
    int a = 10;
    int b = 20;
    int c = a + b;
    return 0;
}
"""

lexer = Lexer(source_code)
parser = Parser(lexer)
semantic_analyzer = SemanticAnalyzer(parser)
intermediate_code_generator = IntermediateCodeGenerator(parser)
optimizer = Optimizer(intermediate_code_generator.intermediate_code)
code_generator = CodeGenerator(optimizer.intermediate_code)

# Ejecutar el compilador
parser.parse()
semantic_analyzer.analyze()
intermediate_code_generator.generate_code()
optimizer.optimize()
machine_code = code_generator.generate_machine_code()
print(machine_code)
