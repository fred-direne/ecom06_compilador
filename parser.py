import ast as ast
from rply import ParserGenerator

class Parser():
    tokens = [
        'IGUAL',
        'MAIOROUIGUAL',
        'MENOROUIGUAL',
        'MENOR',
        'MAIOR',
        'AND',
        'OR',
        'NOT',
        'SOMA',
        'SUBTRACAO',
        'MULTIPLICACAO',
        'DIVISAO',
        'RESTO',
        'ATRIBUICAO',
        'ABREASPAS',
        'FECHAASPAS',
        'PONTO',
        'VIRGULA',
        'DOISPONTOS',
        'PONTOEVIRGULA',
        'ABREPARENTESES',
        'FECHAPARENTESES',
        'ABRECHAVES',
        'FECHACHAVES',
        'INICIOBLOCO',
        'FIMBLOCO',
        'FOR',
        'IF',
        'ELSE',
        'BREAK',
        'WHILE',
        'INT',
        'CHAR',
        'FLOAT',
        'PRINT',
        'READ',
        'REAL',
        'NUMERO',
        'IDENT',
        'CARACTER',
    ]

    precedence = [
        ('left', ['ATRIBUICAO']),
        ('left', [',','.']),
        ('left', ['IF', 'DOISPONTOS', 'ELSE', 'WHILE', 'FOR']),
        ('left', ['AND','OR']),
        ('left', ['NOT']),
        ('left', ['==','!=','<','>', '<=', '>=']),
        ('left', ['SOMA','SUBTRACAO']),
        ('left', ['MULTIPLICACAO','DIVISAO', 'RESTO'])
    ]

    def __init__(self):
        self.pg = ParserGenerator(
            self.tokens,
            precedence=self.precedence
        )

    def parse(self):
        @self.pg.production('program : comando')
        @self.pg.production('program : operacao')
        def program(p):
            return p[0]

        @self.pg.production('comando : decvar PONTOEVIRGULA')
        @self.pg.production('comando : decatrib PONTOEVIRGULA')
        @self.pg.production('comando : decprint PONTOEVIRGULA')
        @self.pg.production('comando : decread PONTOEVIRGULA')
        @self.pg.production('comando : decif PONTOEVIRGULA')
        @self.pg.production('comando : decfor PONTOEVIRGULA')
        @self.pg.production('comando : decwhile PONTOEVIRGULA')
        def comando(p):
            return p[0]

        @self.pg.production('comando : comando comando')
        def comandos(p):
            return p[0] + p[1]

        @self.pg.production('operacao : oprelacional PONTOEVIRGULA')
        @self.pg.production('operacao : oplogico PONTOEVIRGULA')
        @self.pg.production('operacao : oparitmetico PONTOEVIRGULA')
        def operacao(p):
            return p[0]

        @self.pg.production('oparitmetico : IDENT SOMA IDENT')
        @self.pg.production('oparitmetico : IDENT SUBTRACAO IDENT')
        @self.pg.production('oparitmetico : IDENT MULTIPLICACAO IDENT')
        @self.pg.production('oparitmetico : IDENT DIVISAO IDENT')
        @self.pg.production('oparitmetico : IDENT RESTO IDENT')
        def oparitmetico(p):
            left = p[0]
            right = p[2]
            op = p[1]
            if op.gettokentype() == 'SOMA':
                return #funcao ast Sum(left, right)
            elif op.gettokentype() == 'SUBTRACAO':
                return #funcao ast Sub(left, right)
            elif op.gettokentype() == 'MULTIPLICACAO':
                return #funcao ast Sub(left, right)
            elif op.gettokentype() == 'DIVISAO':
                return #funcao ast Sub(left, right)
            elif op.gettokentype() == 'RESTO':
                return #funcao ast Sub(left, right)
        '''
oparitimetico: 
	"ident [( SOMA |
		  SUBTRACAO | 
		  MULTIPLICACAO | 
		  DIVISAO | 
		  RESTO )] ident"

oplogico:
	"(ident [( AND | OR )] ident)|( NOT ident )"

oprelacional:
	"ident [( MENOR | MAIOR | MENOROUIGUAL | MAIOROUIGUAL | IGUAL | DIFERENTE)] ident"


for:
	FOR ABREPARENTESES ident PONTOEVIRGULA operacao PONTOEVIRGULA atribuicao FECHAPARENTESES INICIO BLOCO comando|operacao FIMBLOCO

while:	
	WHILE ABREPARENTESES operacao FECHAPARENTESES INICIOBLOCO comando|operacao
FIMBLOCO

if:
	IF ABREPARENTESES operacao FECHAPARENTESES INICIOBLOCO comando FIMBLOCO ELSE INICIOBLOCO comando|operacao FIMBLOCO

read:
 	"READ ABREPARENTESES ident FECHAPARENTESES"

print:
	"PRINT ABREPARENTESES [(NUMERO* | CARACTER* | ident | oparitmetico)] FECHAPARENTESES "
	
decatrib:
	"(INT | FLOAT | CHAR) ident ATRIBUICAO (NUMERO | REAL | ABREASPAS CARACTER FECHAASPAS’ |ident)"

ident:
	"CARACTER[(NUMERO|CARACTER)]*"

decvar:
	"( INT | FLOAT | CHAR ) ident"


        '''
