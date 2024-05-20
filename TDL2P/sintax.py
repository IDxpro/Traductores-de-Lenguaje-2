import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f'Token({self.type}, {self.value})'

    def __repr__(self):
        return self.__str__()

class Lexer:
    KEYWORDS = {
        "if", "else", "while", "for", "return", "int", "char", "float", "double"
    }

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception("Invalid character")

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_identifier(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()

        if result in self.KEYWORDS:
            return Token(result.upper(), result)
        else:
            return Token("IDENTIFIER", result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isalpha() or self.current_char == '_':
                return self.get_identifier()

            if self.current_char.isdigit():
                return self.get_number()

            if self.current_char == '(':
                self.advance()
                return Token("LPAREN", '(')

            if self.current_char == ')':
                self.advance()
                return Token("RPAREN", ')')

            if self.current_char == '{':
                self.advance()
                return Token("LBRACE", '{')

            if self.current_char == '}':
                self.advance()
                return Token("RBRACE", '}')

            if self.current_char == ';':
                self.advance()
                return Token("SEMICOLON", ';')

            if self.current_char == '=':
                self.advance()
                return Token("ASSIGN", '=')

            if self.current_char == '+':
                self.advance()
                return Token("PLUS", '+')

            self.error()

        return Token("EOF", None)

    def get_number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token("INTEGER", result)

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self, message="Invalid syntax"):
        raise Exception(message)

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(f"Expected token type {token_type}, got {self.current_token.type}")

    def parse_function(self):
        self.eat("INT")  # Assuming return type is int
        self.eat("IDENTIFIER")
        self.eat("LPAREN")
        self.eat("RPAREN")
        self.eat("LBRACE")
        while self.current_token.type != "RBRACE":
            self.parse_statement()
        self.eat("RBRACE")

    def parse_statement(self):
        token = self.current_token

        if token.type in {"INT", "CHAR", "FLOAT", "DOUBLE"}:
            self.eat(token.type)
            self.eat("IDENTIFIER")
            if self.current_token.type == "ASSIGN":
                self.eat("ASSIGN")
                self.parse_expression()
            self.eat("SEMICOLON")
            return True

        if token.type == "IDENTIFIER":
            self.eat("IDENTIFIER")
            self.eat("ASSIGN")
            self.parse_expression()
            self.eat("SEMICOLON")
            return True

        if token.type == "RETURN":
            self.eat("RETURN")
            self.parse_expression()
            self.eat("SEMICOLON")
            return True

        self.error("Invalid statement")

    def parse_expression(self):
        if self.current_token.type == "IDENTIFIER":
            self.eat("IDENTIFIER")
        elif self.current_token.type == "INTEGER":
            self.eat("INTEGER")
        else:
            self.error("Invalid expression")

        while self.current_token.type == "PLUS":
            self.eat("PLUS")
            if self.current_token.type == "IDENTIFIER":
                self.eat("IDENTIFIER")
            elif self.current_token.type == "INTEGER":
                self.eat("INTEGER")
            else:
                self.error("Invalid expression after '+'")

    def parse_program(self):
        while self.current_token.type != "EOF":
            if self.current_token.type == "INT":
                self.parse_function()
            else:
                self.error("Program must start with a function")
        return True

# Example usage:
text = """
int main() {
    int a = 10;
    int b = 20;
    int c = a + b;
    return 0;
}
"""
lexer = Lexer(text)
parser = Parser(lexer)
syntax_valid = parser.parse_program()

if syntax_valid:
    print("Syntax is correct.")
else:
    print("Syntax is incorrect.")
