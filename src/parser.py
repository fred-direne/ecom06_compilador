from rply import ParserGenerator
from src.ast import *
from src.errors import *


class Parser(object):
    tokens = [
        'IGUAL',
        'MAIOROUIGUAL',
        'MENOROUIGUAL',
        'MENOR',
        'MAIOR',
        'DIFERENTE',
        'AND',
        'OR',
        'NOT',
        'SOMA',
        'SUBTRACAO',
        'MULTIPLICACAO',
        'DIVISAO',
        'RESTO',
        'ATRIBUICAO',
        # 'ASPASSIMPLES',
        # 'ASPASDUPLAS',
        # 'PONTO',
        # 'VIRGULA',
        # 'DOISPONTOS',
        'PONTOEVIRGULA',
        'ABREPARENTESES',
        'FECHAPARENTESES',
        # 'ABRECHAVES',
        # 'FECHACHAVES',
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
        'STRING',
        'BOOLEANO',
    ]

    precedence = [
        ('left', ['ATRIBUICAO']),
        ('left', [',', '.']),
        ('left', ['IF', 'INICIOBLOCO', 'ELSE', 'FIMBLOCO', 'WHILE', 'FOR']),
        ('left', ['AND', 'OR']),
        ('left', ['NOT']),
        ('left', ['==', '!=', '>=', '>', '<', '<=']),
        ('left', ['SOMA', 'SUBTRACAO']),
        ('left', ['MULTIPLICACAO', 'DIVISAO', 'RESTO'])
    ]

    def __init__(self):
        self.variables = {}
        self.pg = ParserGenerator(
            self.tokens,
            precedence=self.precedence,
        )

    def parse(self):

        @self.pg.production('main : programa')
        def main_programa(self, p):
            return p[0]

        @self.pg.production('programa : comando_completo')
        def programa_comando(state, p):
            return Programa(p[0])

        @self.pg.production('programa : comando_completo programa')
        def programa_comando_programa(state, p):
            if type(p[1]) is Programa:
                pr = p[1]
            else:
                pr = Programa(p[1])
            pr.add_statement(p[0])
            return p[1]

        @self.pg.production('bloco : comando_completo')
        def bloco_expr(state, p):
            return Block(p[0])

        @self.pg.production('bloco : comando_completo bloco')
        def bloco_expr_bloco(state, p):
            if type(p[1]) is Block:
                b = p[1]
            else:
                b = Block(p[1])

            b.add_statement(p[0])
            return b

        @self.pg.production('comando_completo : comando PONTOEVIRGULA')
        def comando_completo(state, p):
            return p[0]

        @self.pg.production('comando : decprint')
        @self.pg.production('comando : decread')
        @self.pg.production('comando : decatrib')
        @self.pg.production('comando : decvar')
        @self.pg.production('comando : decif')
        @self.pg.production('comando : decfor')
        @self.pg.production('comando : decwhile')
        def comando_function(state, p):
            return p[0]

        @self.pg.production('decwhile : WHILE ABREPARENTESES oprelacional FECHAPARENTESES INICIOBLOCO bloco FIMBLOCO')
        def while_function(state, p):
            return While(condition=p[2], body=p[5])

        @self.pg.production('decfor : FOR ABREPARENTESES decatrib PONTOEVIRGULA oprelacional PONTOEVIRGULA decatrib FECHAPARENTESES INICIOBLOCO bloco FIMBLOCO')
        def for_function(state, p):
            return For(atrib=p[2], condition=p[4], increment=p[6], body=p[9])

        @self.pg.production('decif : IF ABREPARENTESES oprelacional FECHAPARENTESES INICIOBLOCO bloco FIMBLOCO')
        def if_function(state, p):
            return If(condition=p[2], body=p[5])

        @self.pg.production('decif : IF ABREPARENTESES oprelacional FECHAPARENTESES INICIOBLOCO bloco FIMBLOCO ELSE INICIOBLOCO bloco FIMBLOCO')
        def if_else_function(state, p):
            return IfElse(condition=p[2], body=p[5], else_body=p[9])

        @self.pg.production('decprint : PRINT ABREPARENTESES expressao FECHAPARENTESES')
        def print_function(state, p):
            return Print(p[2])

        @self.pg.production('decread : READ ABREPARENTESES IDENT FECHAPARENTESES')
        def read_function(state, p):
            return Read(p[2].getstr())

        @self.pg.production('expressao : expressao SOMA expressao')
        @self.pg.production('expressao : expressao SUBTRACAO expressao')
        @self.pg.production('expressao : expressao MULTIPLICACAO expressao')
        @self.pg.production('expressao : expressao DIVISAO expressao')
        @self.pg.production('expressao : expressao RESTO expressao')
        @self.pg.production('expressao : expressao AND expressao')
        @self.pg.production('expressao : expressao OR expressao')
        def expressao_function(state, p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SOMA':
                return Soma(left, right)
            elif operator.gettokentype() == 'SUBTRACAO':
                return Subtracao(left, right)
            elif operator.gettokentype() == 'MULTIPLICACAO':
                return Multiplicacao(left, right)
            elif operator.gettokentype() == 'DIVISAO':
                return Divisao(left, right)
            elif operator.gettokentype() == 'RESTO':
                return Resto(left, right)
            elif operator.gettokentype() == 'AND':
                return And(left, right)
            elif operator.gettokentype() == 'OR':
                return Or(left, right)
            else:
                raise LogicError('Impossive')

        @self.pg.production('expressao : NOT expressao')
        def notexpressao_function(state, p):
                return Not(p[1])

        @self.pg.production('oprelacional : expressao MENOR expressao')
        @self.pg.production('oprelacional : expressao MAIOR expressao')
        @self.pg.production('oprelacional : expressao MENOROUIGUAL expressao')
        @self.pg.production('oprelacional : expressao MAIOROUIGUAL expressao')
        @self.pg.production('oprelacional : expressao IGUAL expressao')
        @self.pg.production('oprelacional : expressao DIFERENTE expressao')
        def oprelacional_function(state, p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'MENOR':
                return Menor(left, right)
            elif operator.gettokentype() == 'MAIOR':
                return Maior(left, right)
            elif operator.gettokentype() == 'MENOROUIGUAL':
                return MenorOuIgual(left, right)
            elif operator.gettokentype() == 'MAIOROUIGUAL':
                return MaiorOuIgual(left, right)
            elif operator.gettokentype() == 'IGUAL':
                return Igual(left, right)
            elif operator.gettokentype() == 'DIFERENTE':
                return Diferente(left, right)
            else:
                raise LogicError('Impossive')

        @self.pg.production('expressao : IDENT')
        def expressao_ident(state, p):
            return VariavelExpressao(p[0].getstr())

        @self.pg.production('decatrib : IDENT ATRIBUICAO expressao')
        def atribuicao_function(state, p):
            return Atribuicao(p[0].getstr(), p[2])

        @self.pg.production('decvar : INT IDENT')
        @self.pg.production('decvar : FLOAT IDENT')
        @self.pg.production('decvar : CHAR IDENT')
        def declaracao_function(state, p):
            return Declaracao(nome=p[1].getstr(), tipo=p[0].getstr(), value=None)

        @self.pg.production('decvar : INT IDENT ATRIBUICAO NUMERO')
        @self.pg.production('decvar : FLOAT IDENT ATRIBUICAO REAL')
        @self.pg.production('decvar : CHAR IDENT ATRIBUICAO CARACTER')
        def decvarint_function(state, p):
            return Declaracao(nome=p[1].getstr(), tipo=p[0].getstr(), value=p[3].getstr())

        @self.pg.production('expressao : constante')
        def expressao_const(state, p):
            return p[0]

        @self.pg.production('constante : NUMERO')
        def numero_const(state, p):
            return Numero(p[0].value)

        @self.pg.production('constante : REAL')
        def real_const(state, p):
            return Real(p[0].value)

        @self.pg.production('constante : CARACTER')
        def caracter_const(state, p):
            return Caracter(p[0].value)

        @self.pg.production('constante : STRING')
        def string_const(state, p):
            return String(p[0].value)

        @self.pg.production('constante : BOOLEANO')
        def booleano_const(state, p):
            return Booleano(True if p[0].getstr() == 'true' else False)

        @self.pg.error
        def error_handle(state, token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
