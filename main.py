from lexer import Lexer

f = open("exemplo.roberson", "r")

#text_input = f.read()
text_input = "a - 2"
lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

for token in tokens:
    print(token)
