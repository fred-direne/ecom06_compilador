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
        return chr(self.value)


class String():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return str(self.value)


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
        return self.value