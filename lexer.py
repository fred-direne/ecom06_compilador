from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('IGUAL', r'\=\=')
        self.lexer.add('MAIOROUIGUAL', r'\>\=')
        self.lexer.add('MENOROUIGUAL', r'\<\=')
        self.lexer.add('MAIOR', r'\<')
        self.lexer.add('MENOR', r'\!\=')
        self.lexer.add('AND', r'\&')
        self.lexer.add('OR', r'\|')
        self.lexer.add('NOT', r'\!')
        self.lexer.add('SOMA', "+"
SUBTRACAO "−"
MULTIPLICACAO "*"
DIVISAO "/"
RESTO "mod"
ATRIBUICAO "="
ABREASPAS "’"
FECHAASPAS "’"
PONTO "."
VIRGULA ","
DOISPONTOS ":"
PONTOEVIRGULA ";"
ABREPARENTESES "("
FECHAPARENTESES ")"
ABRECHAVES "{"
FECHACHAVES "}"
INICIOBLOCO "begin"
FIMBLOCO "end"
FOR "for"
IF "if"
ELSE "else"
BREAK "break"
WHILE "while"
INT "int"
CHAR "char"
FLOAT "float"
PRINT "print"
READ "read"
NUMERO "[0−9]+"
CARACTER "[a−zA−Z]"
REAL "[0−9]+[.][0−9]+"