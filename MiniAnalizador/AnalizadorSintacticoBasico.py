class SyntaxAnalyzer:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self, message="Syntax error"):
        raise Exception(f"{message}. Unexpected token: {self.current_token.type}, Value: {self.current_token.value}")

    def eat(self, expected_type):
        if self.current_token.type == expected_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(f"Expected {expected_type}")

    def factor(self):
        token = self.current_token

        if token.type == "IDENTIFIER" or token.type == "REAL":
            self.eat(token.type)
        elif token.type == "OpParentesis":
            self.eat("OpParentesis")
            self.expression()
            self.eat("OpParentesis")
        else:
            self.error("Unexpected token in factor")

    def term(self):
        self.factor()

        while self.current_token.type in ["OpMultiplicacion", "OpDivision"]:
            op = self.current_token.value
            self.eat(self.current_token.type)
            self.factor()

    def expression(self):
        self.term()

        while self.current_token.type in ["OpSuma", "OpResta"]:
            op = self.current_token.value
            self.eat(self.current_token.type)
            self.term()

    def parse(self):
        try:
            self.expression()
            print("Syntax analysis successful")
            return True
        except Exception as e:
            print(f"Syntax analysis failed: {e}")
            return False

# Example usage:
text = "abc123 45.67 + 33 - 2 * 3 / 4"
lexer = Lexer(text)
syntax_analyzer = SyntaxAnalyzer(lexer)
success = syntax_analyzer.parse()

if not success:
    print("Handle incorrect input here")
