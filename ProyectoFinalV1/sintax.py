class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self, message="Invalid syntax"):
        raise Exception(message)

    def eat(self, token_type):
        print(f"Expected token type: {token_type}, current token: {self.current_token}")
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(f"Expected token type {token_type}, got {self.current_token.type}")

    def parse_function(self):
        self.eat("INT")  # Assuming return type is int
        self.eat("ID")
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
            self.eat("ID")
            if self.current_token.type == "ASSIGN":
                self.eat("ASSIGN")
                self.parse_expression()
            self.eat("SEMICOLON")
            return True

        if token.type == "ID":
            self.eat("ID")
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
        if self.current_token.type == "ID":
            self.eat("ID")
        elif self.current_token.type == "NUMBER":
            self.eat("NUMBER")
        else:
            self.error("Invalid expression")

        while self.current_token.type in {"PLUS", "MINUS"}:
            self.eat(self.current_token.type)
            if self.current_token.type == "ID":
                self.eat("ID")
            elif self.current_token.type == "NUMBER":
                self.eat("NUMBER")
            else:
                self.error("Invalid expression after operator")

    def parse_program(self):
        while self.current_token.type != "EOF":
            if self.current_token.type == "INT":
                self.parse_function()
            else:
                self.error("Program must start with a function")
        return True
