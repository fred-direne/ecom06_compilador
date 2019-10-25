from src.errors import *

class Numero():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class Real():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return float(self.value)


class Caracter():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return str(self.value).strip("'")


class String():
    def __init__(self, value):
        self.value = value

    def eval(self):
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

    def eval(self):
        result = None
        for statement in self.statements:
            result = statement.eval()
        return result


class Soma(OpBinario):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Subtracao(OpBinario):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Multiplicacao(OpBinario):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Divisao(OpBinario):
    def eval(self):
        return self.left.eval() / self.right.eval()


class Resto(OpBinario):
    def eval(self):
        return self.left.eval() % self.right.eval()

class Menor(OpBinario):
    def eval(self):
        return self.left.eval().lt(self.right.eval())

class Maior(OpBinario):
    def eval(self):
        return self.left.eval().gt(self.right.eval())

class MenorOuIgual(OpBinario):
    def eval(self):
        return self.left.eval().lte(self.right.eval())

class MaiorOuIgual(OpBinario):
    def eval(self):
        return self.left.eval().gte(self.right.eval())

class Igual(OpBinario):
    def eval(self):
        return self.left.eval().equals(self.right.eval())

class Diferente(OpBinario):
    def eval(self):
        result = self.left.eval().equals(self.right.eval())
        result.value = not result.value
        return result

class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())

class Variavel():
    def __init__(self, name, vtype, value=None):
        self.name = name
        self.vtype = vtype
        self.value = value

    def eval(self):
        # este caso so acontece quando declara a variavel sem atribuir valor Ex: int a, float b;
        if self.value is None:
            return None
        else:
            # VALUE GUARDA UM NUMERO() OU REAL() OU CARACTER()
            return self.value.eval()

    def gettype(self):
        return self.vtype