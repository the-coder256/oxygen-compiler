import parser

class Generation:
    def __init__(self):
        self.tree = []
        self.assembly = ""
    
    def generate_exit(self, node):
        self.assembly += "    mov rax, 60\n    mov rdi, " + str(node.arguments[0]) + "\n    syscall\n\n"

    def generate_from_node(self, node):
        if type(node) == parser.Call:
            if node.callee == "exit":
                self.generate_exit(node)
            else:
                print("Not implemented", len(node.callee))
                exit(1)

    def generate(self, __tree):
        self.tree = __tree
        self.assembly += "global _start\n_start:\n"
        for node in self.tree:
            self.generate_from_node(node)
        self.assembly += "    mov rax, 60\n    mov rdi, 0\n    syscall"
        return self.assembly