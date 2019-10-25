FAZ ASSIGNMENT OPERADOR BINARIO ETC ETC
ARQUIVO DO TOKENS FAZER UM IGUAL PARA A GRAMATICA??
ident atrib ident

se conseguir ident atrib operacao

adiciona and or e not somewhere

@pg.production('comando : decvar PONTOEVIRGULA') OK
@pg.production('comando : decatrib PONTOEVIRGULA')
@pg.production('comando : decprint PONTOEVIRGULA') OK
@pg.production('comando : decread PONTOEVIRGULA')
@pg.production('comando : decif PONTOEVIRGULA')
@pg.production('comando : decfor PONTOEVIRGULA')
@pg.production('comando : decwhile PONTOEVIRGULA')
def statement_list_return(self, p):
    return p[0]


@pg.production('decif : IF ABREPARENTESES operacao FECHAPARENTESES INICIOBLOCO listacomando FIMBLOCO')
def if_loop(self, p):
    return If(condition=p[2], body=p[5])


@pg.production(
    'decif : IF ABREPARENTESES operacao FECHAPARENTESES INICIOBLOCO listacomando FIMBLOCO ELSE INICIOBLOCO listacomando FIMBLOCO')
@pg.production('decwhile : WHILE ABREPARENTESES operacao FECHAPARENTESES INICIOBLOCO listacomando FIMBLOCO')
def while_loop(self, p):
    return For(condition=p[2], body=p[5])


@pg.production(
    'decfor : FOR ABREPARENTESES expr PONTOEVIRGULA operacao PONTOEVIRGULA decatrib FECHAPARENTESES INICIOBLOCO listacomando FIMBLOCO')
def for_loop(self, p):
    return For(initial=p[2], condition=p[4], increment=p[6], body=p[9])


@pg.production('decread : READ ABREPARENTESES IDENT FECHAPARENTESES PONTOEVIRGULA')
@pg.production('decprint : PRINT ABREPARENTESES operacao FECHAPARENTESES PONTOEVIRGULA')


def atrib(self, p):
    return Assignment(left=Variable(p[1].getstr()), right=p[3])


@pg.production('decatrib : CHAR IDENT ATRIBUICAO FECHAASPAS CARACTER ABREASPAS IDENT PONTOEVIRGULA')
def atrib(self, p):
    return Assignment(left=Variable(p[1].getstr()), right=p[6])




@pg.production('expr  : expr AND expr PONTOEVIRGULA')
@pg.production('expr  : expr OR expr PONTOEVIRGULA')
@pg.production('expr  : expr NOT expr PONTOEVIRGULA')
@pg.production('expr  : expr MENOR expr PONTOEVIRGULA')
@pg.production('expr  : expr MAIOR expr PONTOEVIRGULA')
@pg.production('expr  : expr MENOROUIGUAL expr PONTOEVIRGULA')
@pg.production('expr  : expr MAIOROUIGUAL expr PONTOEVIRGULA')
@pg.production('expr  : expr IGUAL expr PONTOEVIRGULA')
@pg.production('expr  : expr DIFERENTE expr PONTOEVIRGULA')
def binop(self, p):
    return BinaryOperation(operator=p[1].getstr(), left=p[0], right=p[2])













        @self.pg.production('comando : decvar PONTOEVIRGULA')
        @self.pg.production('comando : decatrib PONTOEVIRGULA')
        @self.pg.production('comando : decprint PONTOEVIRGULA')
        @self.pg.production('comando : decread PONTOEVIRGULA')
        @self.pg.production('comando : decif PONTOEVIRGULA')
        @self.pg.production('comando : decfor PONTOEVIRGULA')
        @self.pg.production('comando : decwhile PONTOEVIRGULA')
        def comando(p):
            return p[0]

        @self.pg.production('operacao : oprelacional PONTOEVIRGULA')
        @self.pg.production('operacao : oplogico PONTOEVIRGULA')
        @self.pg.production('operacao : oparitmetico PONTOEVIRGULA')
        def operacao(p):
            return p[0]

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