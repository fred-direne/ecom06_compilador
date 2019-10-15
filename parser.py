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

        
