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

       if result in ["if", "else", "while", "for", "return", "main", "int", "char", "real"]:  # Check for keywords
           return Token(result.upper(), result)  # Return with uppercase type
       else:
           return Token("IDENTIFIER", result)

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
    
   def OpParentesis(self):
        result = ''
        while self.current_char is not None and (self.current_char == "(" or self.current_char == ")"):
            result += self.current_char
            self.advance()
        return result
    
   def OpCorchetes(self):
        result = ''
        while self.current_char is not None and (self.current_char == "{" or self.current_char == "}"):
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
    
   def OPOr(self):
        result = ''
        while self.current_char is not None and (self.current_char == "|"):
            result += self.current_char
            self.advance()
        return result
    
   def OpIgualdad(self):
        result = ''
        while self.current_char is not None and (self.current_char == "="):
            result += self.current_char
            self.advance()
        return result
    
   def OpPuntoComa(self):
        result = ''
        while self.current_char is not None and (self.current_char == ";"):
            result += self.current_char
            self.advance()
        return result
    
   def OpIf(self):
        result = ''
        while self.current_char is not None and (self.current_char == "If"):
            result += self.current_char
            self.advance()
        return result
    
   def OpWhile(self):
        result = ''
        while self.current_char is not None and (self.current_char == "While"):
            result += self.current_char
            self.advance()
        return result
    
   def OpReturn(self):
        result = ''
        while self.current_char is not None and (self.current_char == "Return"):
            result += self.current_char
            self.advance()
        return result
    
   def OpElse(self):
        result = ''
        while self.current_char is not None and (self.current_char == "Else"):
            result += self.current_char
            self.advance()
        return result
    
   def OpFloat(self):
        result = ''
        while self.current_char is not None and (self.current_char == "float"):
            result += self.current_char
            self.advance()
        return result

   def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isalpha():
               return self.get_identifier() #addifelse

            if self.current_char.isdigit():
                return Token("REAL", self.get_real()) #addifelse for a dot
            
            if self.current_char == "+" or self.current_char == "-":
                return Token("OpSuma", self.OPsuma())
            
            if self.current_char == "*" or self.current_char == "/":
                return Token("OpMultiplicacion", self.OPmultiplicacion())
            
            if self.current_char == "<" or self.current_char == ">": #addifelse
                return Token("OpRelac", self.OPRelac())
            
            if self.current_char == "!":
                return Token("OpNot", self.OPNot())
            
            if self.current_char == "&": 
                return Token("OpAnd", self.OPAnd())
            
            if self.current_char == "|": 
                return Token("OpOr", self.OPOr())
            
            if self.current_char == "=": 
                return Token("OpIgualdad", self.OpIgualdad())
            
            if self.current_char == "(" or self.current_char == ")":
                return Token("OpParentesis", self.OpParentesis())
            
            if self.current_char == "{" or self.current_char == "}":
                return Token("OpCorchetes", self.OpCorchetes())
            
            if self.current_char == ";": 
                return Token("OpPuntoComa", self.OpPuntoComa())
            
            if self.current_char == "if": 
                return Token("OpIf", self.OpIf())
            
            if self.current_char == "while": 
                return Token("OpWhile", self.OpWhile())
            
            if self.current_char == "return": 
                return Token("OpReturn", self.OpReturn())
            
            if self.current_char == "else": 
                return Token("OpElse", self.OpElse())
            
            if self.current_char == "int": 
                return Token("OpInt", self.OpInt())
            
            if self.current_char == "float": 
                return Token("OpFloat", self.OpFloat())

            self.error()

        return Token("EOF", None)

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

while True:
    token = lexer.get_next_token()
    if token.type == "EOF":
        break
    print(f"Token: {token.type}, Value: {token.value}")
    
