from sys import argv
import tokeniser
import parser
import generation

if len(argv) < 2:
    print("No file given")
    exit(1)

with open(argv[1], "r") as in_file:
    contents = in_file.read()

tokens = tokeniser.Tokeniser().tokenise(contents)
tree = parser.Parser().parse(tokens)
assembly = generation.Generation().generate(tree)

with open("output.asm", "w") as out_file:
    out_file.write(assembly)