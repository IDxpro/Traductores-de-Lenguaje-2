class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        self.current_token = self.tokens[self.current_token_index]
        print(f"Initial token: {self.current_token}")

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

    def parse_program(self):
        print("Parsing program")
        while self.current_token:
            print(f"Current token in parse_program: {self.current_token}")
            if self.current_token.type == "INT":
                self.parse_function()
            else:
                self.error("Program must start with a function")
        return True
