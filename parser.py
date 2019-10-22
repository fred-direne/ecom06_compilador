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
                return ast.Sum(left, right)
            elif op.gettokentype() == 'SUBTRACAO':
                return #funcao ast Sub(left, right)
            elif op.gettokentype() == 'MULTIPLICACAO':
                return #funcao ast Sub(left, right)
            elif op.gettokentype() == 'DIVISAO':
                return #funcao ast Sub(left, right)
            elif op.gettokentype() == 'RESTO':
                return #funcao ast Sub(left, right)
        @self.pg.production('oplogico : IDENT AND IDENT')
        @self.pg.production('oplogico : IDENT OR IDENT')
        @self.pg.production('oplogico : NOT IDENT')
        
        @self.pg.production('oprelacional : IDENT MENOR IDENT')
        @self.pg.production('oprelacional : IDENT MAIOR IDENT')
        @self.pg.production('oprelacional : IDENT MENOROUIGUAL IDENT')
        @self.pg.production('oprelacional : IDENT MAIOROUIGUAL IDENT')
        @self.pg.production('oprelacional : IDENT IGUAL IDENT')
        @self.pg.production('oprelacional : IDENT DIFERENTE IDENT')
        
        @self.pg.production('for : FOR ABREPARENTESES IDENT PONTOEVIRGULA operacao PONTOEVIRGULA atribuicao FECHAPARENTESES INICIOBLOCO comando FIMBLOCO')
        
        @self.pg.production('while : WHILE ABREPARENTESES operacao FECHAPARENTESES INICIOBLOCO comando FIMBLOCO')
        
        @self.pg.production('if : IF ABREPARENTESES operacao FECHAPARENTESES INICIOBLOCO comando FIMBLOCO ELSE INICIOBLOCO comando FIMBLOCO')
        
        @self.pg.production('read : READ ABREPARENTESES ident FECHAPARENTESES')
        
        @self.pg.production('print : PRINT ABREPARENTESES NUMERO FECHAPARENTESES')
        @self.pg.production('print : PRINT ABREPARENTESES CARACTER FECHAPARENTESES')
        @self.pg.production('print : PRINT ABREPARENTESES ident FECHAPARENTESES')
        @self.pg.production('print : PRINT ABREPARENTESES oparitmetico FECHAPARENTESES')
        
        @self.pg.production('decatrib : INT IDENT ATRIBUICAO NUMERO')
        @self.pg.production('decatrib : INT IDENT ATRIBUICAO IDENT')
        @self.pg.production('decatrib : FLOAT IDENT ATRIBUICAO REAL')
        @self.pg.production('decatrib : FLOAT IDENT ATRIBUICAO IDENT')
        @self.pg.production('decatrib : CHAR IDENT ATRIBUICAO ABREASPAS CARACTER FECHAASPAS')
        @self.pg.production('decatrib : CHAR IDENT ATRIBUICAO IDENT')

        @self.pg.production('decvar : INT IDENT')
        @self.pg.production('decvar : FLOAT IDENT')
        @self.pg.production('decvar : CHAR IDENT')
