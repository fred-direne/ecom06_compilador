from src.lexer import Lexer
from src.parser import Parser

f = open("notas.roberson", "r")
text_input = f.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)
tokens2 = lexer.lex(text_input)

out_tokens = open("lista_tokens.txt", "w")
for token in tokens2:
    out_tokens.write(str(token) + "\n")

pg = Parser()
pg.parse()
parser = pg.get_parser()
res = parser.parse(tokens, state=Parser())
print(res.eval(Parser()))
