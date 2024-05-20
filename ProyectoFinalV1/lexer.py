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
            return Token("ID", result)

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

            if self.current_char == '-':
                self.advance()
                return Token("MINUS", '-')

            self.error()

        return Token("EOF", None)

    def get_number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token("NUMBER", result)
