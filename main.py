#from lib2to3.pgen2.tokenize import generate_tokens
from lexer import Lexer
from parser_ import Parser

while True:
    text = input ("calculator > ")
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    token_lst = list(tokens)
    print(token_lst)

    parser = Parser(token_lst)
    tree=parser.parse()
    print(tree.eval())