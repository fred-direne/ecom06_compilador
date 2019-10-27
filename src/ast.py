from src.errors import *


class Programa():
    def __init__(self, statement):
        self.statements = []
        self.statements.append(statement)

    def add_statement(self, statement):
        self.statements.insert(0, statement)

    def eval(self, env):
        result = None
        for statement in self.statements:
            result = statement.eval(env)
        return result

    def get_statements(self):
        return self.statements


class Booleano():
    def __init__(self, value):
        self.value = value

    def eval(self, env):
        return bool(self.value)


class Numero():
    def __init__(self, value):
        self.value = value

    def eval(self, env):
        return int(self.value)


class Real():
    def __init__(self, value):
        self.value = value

    def eval(self, env):
        return float(self.value)


class Caracter():
    def __init__(self, value):
        self.value = value

    def eval(self, env):
        return str(self.value).strip("'")


class String():
    def __init__(self, value):
        self.value = value

    def eval(self, env):
        return str(self.value).strip("\"")


class OpBinario():
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Block():
    def __init__(self, statement):
        self.statements = []
        self.statements.append(statement)

    def add_statement(self, statement):
        self.statements.insert(0, statement)

    def eval(self, env):
        result = None
        for statement in self.statements:
            result = statement.eval(env)
        return result

    def get_statements(self):
        return self.statements


class Soma(OpBinario):
    def eval(self, env):
        return self.left.eval(env) + self.right.eval(env)



class Subtracao(OpBinario):
    def eval(self, env):
        return self.left.eval(env) - self.right.eval(env)


class Multiplicacao(OpBinario):
    def eval(self, env):
        return self.left.eval(env) * self.right.eval(env)


class Divisao(OpBinario):
    def eval(self, env):
        return self.left.eval(env) / self.right.eval(env)


class Resto(OpBinario):
    def eval(self, env):
        return self.left.eval(env) % self.right.eval(env)


class Menor(OpBinario):
    def eval(self, env):
        return self.left.eval(env) < self.right.eval(env)


class Maior(OpBinario):
    def eval(self, env):
        return self.left.eval(env) > self.right.eval(env)


class MenorOuIgual(OpBinario):
    def eval(self, env):
        return self.left.eval(env) <= self.right.eval(env)


class MaiorOuIgual(OpBinario):
    def eval(self, env):
        return self.left.eval(env) >= self.right.eval(env)


class Igual(OpBinario):
    def eval(self, env):
        return self.left.eval(env) == self.right.eval(env)


class Diferente(OpBinario):
    def eval(self, env):
        return self.left.eval(env) != self.right.eval(env)


class And(OpBinario):
    def eval(self, env):
        return self.left.eval(env) and self.right.eval(env)


class Or(OpBinario):
    def eval(self, env):
        return self.left.eval(env) or self.right.eval(env)


class Not():
    def __init__(self, value):
        self.value = value

    def eval(self, env):
        return not self.value.eval(env)


class Print():
    def __init__(self, value):
        self.value = value

    def eval(self, env):
        print(self.value.eval(env))

class If():
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def eval(self, env):
        condition = self.condition.eval(env)
        if condition:
            return self.body.eval(env)


class IfElse():
    def __init__(self, condition, body, else_body):
        self.condition = condition
        self.body = body
        self.else_body = else_body

    def eval(self, env):
        condition = self.condition.eval(env)
        if condition:
            return self.body.eval(env)
        else:
            return self.else_body.eval(env)


class While():
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def eval(self, env):
        while self.condition.eval(env):
            self.body.eval(env)

class For():
    def __init__(self, atrib, condition, increment, body):
        self.atrib = atrib
        self.condition = condition
        self.increment = increment
        self.body = body

    def eval(self, env):
        self.atrib.eval(env)
        while self.condition.eval(env):
            self.body.eval(env)
            self.increment.eval(env)


class Variavel():
    def __init__(self, nome, tipo, value):
        self.nome = nome
        self.tipo = tipo
        self.value = value

    def eval(self, env):
        if env.variables.get(self.nome) is not None:
            self.value = env.variables[self.nome].eval(env)
            return self.value
        raise LogicError("Not yet defined")

class VariavelExpressao():
    def __init__(self, nome):
        self.nome = nome

    def eval(self, env):
        if env.variables.get(self.nome) is not None:
            return env.variables[self.nome].value.eval(env)
        raise LogicError("Variavel nao definida")

class Declaracao():
    def __init__(self, nome, tipo, value):
        self.nome = nome
        self.tipo = tipo
        self.value = value

    def eval(self, env):
        if env.variables.get(self.nome) is None:
            if self.tipo == "int":
                env.variables[self.nome] = Variavel(nome=self.nome, tipo=self.tipo, value=Numero(self.value))
            elif self.tipo == "float":
                env.variables[self.nome] = Variavel(nome=self.nome, tipo=self.tipo, value=Real(self.value))
            elif self.tipo == "char":
                env.variables[self.nome] = Variavel(nome=self.nome, tipo=self.tipo, value=Caracter(self.value))
        else:
            raise LogicError("Variavel ja foi definida")

class Atribuicao(OpBinario):
    def eval(self, env):
        if env.variables.get(self.left) is not None:

            if env.variables[self.left].tipo == "int":
                env.variables[self.left].value = Numero(self.right.eval(env))
            elif env.variables[self.left].tipo == "float":
                env.variables[self.left].value = Real(self.right.eval(env))
            elif env.variables[self.left].tipo == "char":
                env.variables[self.left].value = Caracter(self.right.eval(env))

            return env.variables[self.left].value
        else:
            raise LogicError("Variavel nao definida")

class Read():
    def __init__(self, nome):
        self.nome = nome

    def eval(self, env):
        v = env.variables.get(self.nome)
        if v is not None:
            valorlido = input()
            if v.tipo == "int":
                env.variables[self.nome].value = Numero(int(valorlido))
                return Numero(int(valorlido))
            elif v.tipo == "float":
                env.variables[self.nome].value = Real(float(valorlido))
                return Real(float(valorlido))
            elif v.tipo == "char":
                env.variables[self.nome].value = Caracter(str(valorlido))
                return Caracter(str(valorlido))

        else:
            raise LogicError("Variavel nao existe")