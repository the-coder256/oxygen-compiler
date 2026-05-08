import tokeniser

class Call:
    def __init__(self, callee:str, arguments:list):
        self.callee = callee
        self.arguments = arguments

class Parser:
    def __init__(self):
        self.tokens = []
        self.tree = []
        self.index = 0
    
    def peek(self, amount):
        try:
            return self.tokens[self.index + amount]
        except:
            return tokeniser.T_End("END")

    def consume(self):
        return self.tokens[self.index]

    def advance(self):
        self.index += 1
        return self.tokens[self.index - 1]

    def at_end(self):
        return type(self.consume()) == tokeniser.T_End
    
    def parse_function_call(self):
        callee = self.peek(-1).value
        self.advance()
        arguments = [self.advance().value]
        if type(self.advance()) != tokeniser.T_RightParen:
            print("Expected ')'")
            exit(1)
        return Call(callee, arguments)

    def parse_stmt(self):
        beginning = self.advance()
        if type(beginning) == tokeniser.T_Ident and type(self.consume()) == tokeniser.T_LeftParen:
            return self.parse_function_call()

    def parse(self, __tokens):
        self.tokens = __tokens
        while not self.at_end():
            node = self.parse_stmt()
            self.tree.append(node)
        return self.tree