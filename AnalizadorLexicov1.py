import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Lexer:
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
        while self.current_char is not None and (self.current_char.isalpha() or self.current_char.isdigit()):
            result += self.current_char
            self.advance()
        return result

    def get_real(self):
        integer_part = ''
        decimal_part = ''
        
        while self.current_char is not None and self.current_char.isdigit():
            integer_part += self.current_char
            self.advance()
        
        if self.current_char == '.':
            self.advance()
            
            while self.current_char is not None and self.current_char.isdigit():
                decimal_part += self.current_char
                self.advance()

        if integer_part and decimal_part:
            return float(f"{integer_part}.{decimal_part}")
        elif integer_part:
            return int(f"{integer_part}")
        else:
            self.error()
            
    def OPsuma(self):
        result = ''
        while self.current_char is not None and (self.current_char == "+" or self.current_char == "-"):
            result += self.current_char
            self.advance()
        return result
    
    def OPmultiplicacion(self):
        result = ''
        while self.current_char is not None and (self.current_char == "*" or self.current_char == "/"):
            result += self.current_char
            self.advance()
        return result
    
    def OPRelac(self):
        result = ''
        while self.current_char is not None and (self.current_char == "<" or self.current_char == "<="):
            result += self.current_char
            self.advance()
        return result
    
    def OPNot(self):
        result = ''
        while self.current_char is not None and (self.current_char == "!"):
            result += self.current_char
            self.advance()
        return result
    
    def OPAnd(self):
        result = ''
        while self.current_char is not None and (self.current_char == "&"):
            result += self.current_char
            self.advance()
        return result

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isalpha():
                return Token("IDENTIFIER", self.get_identifier())

            if self.current_char.isdigit():
                return Token("REAL", self.get_real())
            
            if self.current_char == "+" or self.current_char == "-":
                return Token("OpSuma", self.OPsuma())
            
            if self.current_char == "*" or self.current_char == "/":
                return Token("OpMultiplicacion", self.OPmultiplicacion())
            
            if self.current_char == "<" or self.current_char == ">":
                return Token("OpRelac", self.OPRelac())
            
            if self.current_char == "!":
                return Token("OpNot", self.OPNot())
            
            if self.current_char == "&": #Modify for two characters
                return Token("OpAnd", self.OPAnd())

            self.error()

        return Token("EOF", None)

# Example usage:
text = "abc123 45.67 x 33 + - 2 < / 3 ! &"
lexer = Lexer(text)

while True:
    token = lexer.get_next_token()
    if token.type == "EOF":
        break
    print(f"Token: {token.type}, Value: {token.value}")

