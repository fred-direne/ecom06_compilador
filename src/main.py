from src.lexer import Lexer
from src.parser import Parser

f = open("exemplo.roberson", "r")
text_input = f.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
res = parser.parse(tokens, state=Parser())
print(res.eval(Parser()))
