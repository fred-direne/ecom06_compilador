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
        def main_programa(p):
            return p[0]

        @self.pg.production('programa : comando_completo')
        def programa_comando(p):
            return Programa(p[0])

        @self.pg.production('programa : comando_completo programa')
        def programa_comando_programa(p):
            if type(p[1]) is Programa:
                pr = p[1]
            else:
                pr = Programa(p[1])
            pr.add_statement(p[0])
            return p[1]

        @self.pg.production('bloco : comando_completo')
        def bloco_expr(p):
            return Block(p[0])

        @self.pg.production('bloco : comando_completo bloco')
        def bloco_expr_bloco(p):
            if type(p[1]) is Block:
                b = p[1]
            else:
                b = Block(p[1])

            b.add_statement(p[0])
            return b

        @self.pg.production('comando_completo : comando PONTOEVIRGULA')
        def comando_completo(p):
            return p[0]

        @self.pg.production('comando : decprint')
        @self.pg.production('comando : decvar')
        @self.pg.production('comando : decatrib')
        @self.pg.production('comando : decread')
<<<<<<< HEAD
        def comando_function(p):
            return p[0]

        @self.pg.production('comando : WHILE ABREPARENTESES oprelacional FECHAPARENTESES INICIOBLOCO bloco FIMBLOCO')
=======
        @self.pg.production('comando : decwhile')
        @self.pg.production('comando : decif')
        def comando_function(p):
            return p[0]

        @self.pg.production('decif : IF ABREPARENTESES oprelacional FECHAPARENTESES INICIOBLOCO listacomando FIMBLOCO')
        def if_function(p):
            return If(condition=p[2], body=p[5])

        @self.pg.production('decif : IF ABREPARENTESES oprelacional FECHAPARENTESES INICIOBLOCO listacomando FIMBLOCO ELSE INICIOBLOCO listacomando FIMBLOCO')
        def if_else_function(p):
            return IfElse(condition=p[2], body=p[5], else_body=p[9])

        @self.pg.production('decwhile : WHILE ABREPARENTESES oprelacional FECHAPARENTESES INICIOBLOCO listacomando FIMBLOCO')
>>>>>>> master
        def while_function(p):
            print(p)
            return p[2]

        @self.pg.production('decprint : PRINT ABREPARENTESES expressao FECHAPARENTESES')
        def print_function(p):
            return Print(p[2])

        @self.pg.production('decread : READ ABREPARENTESES IDENT FECHAPARENTESES')
        def read_function(p):
            if self.variables.get(p[2].getstr()) is not None:
                valorlido = input()
                if self.variables.get(p[2].getstr()).gettype() == "int":
                    self.variables[p[2].getstr()].value = Numero(int(valorlido))
                    return Numero(int(valorlido))
                elif self.variables.get(p[2].getstr()).gettype() == "float":
                    self.variables[p[2].getstr()].value = Real(float(valorlido))
                    return Real(float(valorlido))
                elif self.variables.get(p[2].getstr()).gettype() == "char":
                    self.variables[p[2].getstr()].value = Caracter(str(valorlido))
                    return Caracter(str(valorlido))
            else:
                raise ImmutableError("Variavel nao foi declarada nao da pra atribuir valor")

        @self.pg.production('decatrib : IDENT ATRIBUICAO expressao')
        def atribuicao_function(p):
            if self.variables.get(p[0].getstr()) is not None:
                if self.variables.get(p[0].getstr()).gettype() == "int":
                    self.variables[p[0].getstr()].value = Numero(p[2].eval())
                elif self.variables.get(p[0].getstr()).gettype() == "float":
                    self.variables[p[0].getstr()].value = Real(p[2].eval())
                elif self.variables.get(p[0].getstr()).gettype() == "char":
                    self.variables[p[0].getstr()].value = Caracter(p[2].eval())
                else:
                    raise LogicError("Tipo de variavel diferente")
                return p[2]
            else:
                raise ImmutableError("Variavel nao foi declarada nao da pra atribuir valor")

        @self.pg.production('decvar : INT IDENT')
        @self.pg.production('decvar : FLOAT IDENT')
        @self.pg.production('decvar : CHAR IDENT')
        def declaracao_function(p):
            name = p[1].getstr()
            if self.variables.get(name) is not None:
                raise LogicError("Variable already declared")
            else:
                v = Variavel(name=p[1].getstr(), vtype=p[0].getstr(), value=None)
                self.variables[name] = v
            return v

        @self.pg.production('decvar : INT IDENT ATRIBUICAO NUMERO')
        def decvarint_function(p):
            name = p[1].getstr()
            if self.variables.get(name) is not None:
                raise LogicError("Variable already declared")
            else:
                v = Variavel(name=p[1].getstr(), vtype=p[0].getstr(), value=Numero(p[3].value))
                self.variables[name] = v
            return v

        @self.pg.production('decvar : FLOAT IDENT ATRIBUICAO REAL')
        def decvarfloat_function(p):
            name = p[1].getstr()
            if self.variables.get(name) is not None:
                raise LogicError("Variable already declared")
            else:
                v = Variavel(name=p[1].getstr(), vtype=p[0].getstr(), value=Real(p[3].value))
                self.variables[name] = v
            return v

        @self.pg.production('decvar : CHAR IDENT ATRIBUICAO CARACTER')
        def decvarchar_function(p):
            name = p[1].getstr()
            if self.variables.get(name) is not None:
                raise LogicError("Variable already declared")
            else:
                v = Variavel(name=p[1].getstr(), vtype=p[0].getstr(), value=Caracter(p[3].value))
                self.variables[name] = v
            return v

        @self.pg.production('expressao  : expressao SOMA expressao')
        @self.pg.production('expressao  : expressao SUBTRACAO expressao')
        @self.pg.production('expressao  : expressao MULTIPLICACAO expressao')
        @self.pg.production('expressao  : expressao DIVISAO expressao')
        @self.pg.production('expressao  : expressao RESTO expressao')
        @self.pg.production('expressao  : expressao AND expressao')
        @self.pg.production('expressao  : expressao OR expressao')
        def expressao_function(p):
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
                raise LogicError('Oops, this should not be possible!')

        @self.pg.production('expressao  : NOT expressao')
        def notexpressao_function(p):
                return Not(p[1])

        @self.pg.production('oprelacional  : expressao MENOR expressao')
        @self.pg.production('oprelacional  : expressao MAIOR expressao')
        @self.pg.production('oprelacional  : expressao MENOROUIGUAL expressao')
        @self.pg.production('oprelacional  : expressao MAIOROUIGUAL expressao')
        @self.pg.production('oprelacional  : expressao IGUAL expressao')
        @self.pg.production('oprelacional  : expressao DIFERENTE expressao')
        def oprelacional_function(p):
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
                raise LogicError('Oops, this should not be possible!')

        @self.pg.production('expressao : IDENT')
        def expressao_ident(p):
            name = p[0].getstr()
            v = self.variables.get(name)
            if v is None:
                raise LogicError("Variable not found")
            else:
                return v

        @self.pg.production('expressao : constante')
        def expressao_const(p):
            return p[0]

        @self.pg.production('constante : NUMERO')
        def numero_const(p):
            return Numero(p[0].value)

        @self.pg.production('constante : REAL')
        def real_const(p):
            return Real(p[0].value)

        @self.pg.production('constante : CARACTER')
        def caracter_const(p):
            return Caracter(p[0].value)

        @self.pg.production('constante : STRING')
        def string_const(p):
            return String(p[0].value)

        @self.pg.production('constante : BOOLEANO')
        def booleano_const(p):
            return Booleano(True if p[0].getstr() == 'true' else False)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
