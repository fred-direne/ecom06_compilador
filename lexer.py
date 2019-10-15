from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('REAL', r'-?\d+[.]\d+')
        self.lexer.add('NUMERO', r'-?\d+')
        self.lexer.add('IGUAL', r'\==')
        self.lexer.add('MAIOROUIGUAL', r'\>=')
        self.lexer.add('MENOROUIGUAL', r'\<=')
        self.lexer.add('MENOR', r'\<')
        self.lexer.add('MAIOR', r'\>')
        self.lexer.add('DIFERENTE', r'\!=')
        self.lexer.add('AND', r'\&')
        self.lexer.add('OR', r'\|')
        self.lexer.add('NOT', r'\!')
        self.lexer.add('SOMA', r'\+')
        self.lexer.add('SUBTRACAO', r"\−")
        self.lexer.add('MULTIPLICACAO', r'\*')
        self.lexer.add('DIVISAO', r'\/')
        self.lexer.add('RESTO', r'mod')
        self.lexer.add('ATRIBUICAO', r'\=')
        self.lexer.add('ABREASPAS', r'\’')
        self.lexer.add('FECHAASPAS', r'\’')
        self.lexer.add('PONTO', '\.')
        self.lexer.add('VIRGULA', '\,')
        self.lexer.add('DOISPONTOS', r'\:')
        self.lexer.add('PONTOEVIRGULA',  r'\;')
        self.lexer.add('ABREPARENTESES', r'\(')
        self.lexer.add('FECHAPARENTESES', r'\)')
        self.lexer.add('ABRECHAVES', r'\{')
        self.lexer.add('FECHACHAVES', r'\}')
        self.lexer.add('INICIOBLOCO', r'begin')
        self.lexer.add('FIMBLOCO', r'end')
        self.lexer.add('FOR',  r'for')
        self.lexer.add('IF', r'if')
        self.lexer.add('ELSE', r'else')
        self.lexer.add('BREAK', r'break')
        self.lexer.add('WHILE', r'while')
        self.lexer.add('INT', r'int')
        self.lexer.add('CHAR', r'char')
        self.lexer.add('FLOAT', r'float')
        self.lexer.add('PRINT', r'print')
        self.lexer.add('READ', r'read')
        self.lexer.add('IDENT', r'[a-zA-Z][a-zA-Z0-9]*')
        self.lexer.add('CARACTER', r'[a−zA−Z]+')

        #Ignore spaces
        self.lexer.ignore('[\s\t]+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()




