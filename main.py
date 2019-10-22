from lexer import Lexer
from parse import Parser

f = open("exemplo.roberson", "r")

#text_input = f.read()
text_input = "print(2);"

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()

for token in tokens:
    print(token)
