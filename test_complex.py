from antlr4 import *
from ComplexLexer import ComplexLexer
from ComplexParser import ComplexParser

def main():
    input_stream = InputStream("(2 + 7i) + (3 - 4i)")
    lexer = ComplexLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ComplexParser(stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))

if __name__ == "__main__":
    main()

