class T_Int:
    def __init__(self, value):
        self.value = value
class T_Ident:
    def __init__(self, value):
        self.value = value
class T_LeftParen:
    def __init__(self, value):
        self.value = value
class T_RightParen:
    def __init__(self, value):
        self.value = value
class T_End:
    def __init__(self, value):
        self.value = value

class Tokeniser:
    def __init__(self):
        self.tokens = []
        self.contents = ""
        self.current_token = ""
    
    def create_token(self, value):
        tok_type = T_End      # temporary
        if value == "(":
            tok_type = T_LeftParen
        elif value == ")":
            tok_type = T_RightParen
        else:
            try:
                x = int(value)
                tok_type = T_Int
            except:
                tok_type = T_Ident
        return tok_type(value)

    def append_token(self, __extra):
        self.tokens.append(self.create_token(self.current_token))
        self.tokens.append(self.create_token(__extra))
        self.current_token = ""
    
    def tokenise(self, __contents):
        self.contents = __contents
        for index in range(len(self.contents)):
            char = self.contents[index]
            if char == "\n":
                continue
            elif char == "(":
                self.append_token("(")
            elif char == ")":
                self.append_token(")")
            else:
                self.current_token += char
        if self.current_token != "":
            self.tokens.append(self.create_token(self.current_token))
        self.tokens.append(T_End("END"))
        return self.tokens