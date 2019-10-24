from rply import ParserGenerator
from src.ast import *
from src.errors import *

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
        'STRING',
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
        self.variables = {}
        self.pg = ParserGenerator(
            self.tokens,
            precedence=self.precedence,
        )

    def parse(self):

        @self.pg.production('programa : listacomando')
        def programa(p):
            return p[0]

        @self.pg.production('listacomando : comando PONTOEVIRGULA')
        def listacomando_simples(p):
            return Block(p[0])

        @self.pg.production('listacomando : comando  PONTOEVIRGULA listacomando')
        def listacomando_bloco(p):
            if type(p[2]) is Block:
                b = p[2]
            else:
                b = Block(p[2])

            b.add_statement(p[0])
            return b

        @self.pg.production('comando : decprint')
        @self.pg.production('comando : decvar')
        def comando_function(p):
            return p[0]

        @self.pg.production('decprint : PRINT ABREPARENTESES operacao FECHAPARENTESES')
        def print_function(p):
            return Print(p[2])

        @self.pg.production('decvar : INT IDENT')
        @self.pg.production('decvar : FLOAT IDENT')
        @self.pg.production('decvar : CHAR IDENT')
        def declaracao_function(p):
            name = p[1].getstr()
            if self.variables.get(name) is not None:
                raise LogicError("Variable already declared")
            else:
                v = Variavel(name=p[1].getstr(), vtype=p[0], value=None)
                self.variables[name] = v
            return v

        @self.pg.production('decvar : INT IDENT ATRIBUICAO NUMERO')
        def decvarint_function(p):
            name = p[1].getstr()
            if self.variables.get(name) is not None:
                raise LogicError("Variable already declared")
            else:
                v = Variavel(name=p[1].getstr(), vtype=p[0], value=Numero(p[3].value))
                self.variables[name] = v
            return v

        @self.pg.production('decvar : FLOAT IDENT ATRIBUICAO REAL')
        def decvarfloat_function(p):
            name = p[1].getstr()
            if self.variables.get(name) is not None:
                raise LogicError("Variable already declared")
            else:
                v = Variavel(name=p[1].getstr(), vtype=p[0], value=Real(p[3].value))
                self.variables[name] = v
            return v

        @self.pg.production('decvar : CHAR IDENT ATRIBUICAO CARACTER')
        def decvarchar_function(p):
            name = p[1].getstr()
            if self.variables.get(name) is not None:
                raise LogicError("Variable already declared")
            else:
                v = Variavel(name=p[1].getstr(), vtype=p[0], value=Caracter(p[3].value))
                self.variables[name] = v
            return v

        @self.pg.production('operacao  : operacao SOMA operacao')
        @self.pg.production('operacao  : operacao SUBTRACAO operacao')
        @self.pg.production('operacao  : operacao MULTIPLICACAO operacao')
        @self.pg.production('operacao  : operacao DIVISAO operacao')
        @self.pg.production('operacao  : operacao RESTO operacao')
        def operacao_function(p):
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
            else:
                raise LogicError('Oops, this should not be possible!')

        @self.pg.production('operacao : IDENT')
        def operacao_ident(p):
            name = p[0].getstr()
            if self.variables.get(name) is None:
                raise LogicError("Variable not found")
            else:
                return self.variables.get(name).eval()

        @self.pg.production('operacao : constante')
        def operacao_const(p):
            return p[0]

        @self.pg.production('constante : NUMERO')
        def numero(p):
            return Numero(p[0].value)

        @self.pg.production('constante : REAL')
        def real(p):
            return Real(p[0].value)

        @self.pg.production('constante : CARACTER')
        def caractere(p):
            return Caracter(p[0].value)

        @self.pg.production('constante : STRING')
        def string_const(p):
            return String(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()