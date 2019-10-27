ARQUIVO DO TOKENS FAZER UM IGUAL PARA A GRAMATICA
ident atrib ident
se conseguir ident atrib operacao

@pg.production('comando : decif PONTOEVIRGULA')
@pg.production('comando : decfor PONTOEVIRGULA')
@pg.production('comando : decwhile PONTOEVIRGULA')
def statement_list_return(self, p):
    return p[0]


@pg.production('decif : IF ABREPARENTESES operacao FECHAPARENTESES INICIOBLOCO listacomando FIMBLOCO')
def if_loop(self, p):
    return If(condition=p[2], body=p[5])


@pg.production('decif : IF ABREPARENTESES operacao FECHAPARENTESES INICIOBLOCO listacomando FIMBLOCO ELSE INICIOBLOCO listacomando FIMBLOCO')
@pg.production('decwhile : WHILE ABREPARENTESES operacao FECHAPARENTESES INICIOBLOCO listacomando FIMBLOCO')
def while_loop(self, p):
    return For(condition=p[2], body=p[5])


@pg.production('decfor : FOR ABREPARENTESES expr PONTOEVIRGULA operacao PONTOEVIRGULA decatrib FECHAPARENTESES INICIOBLOCO listacomando FIMBLOCO')
def for_loop(self, p):
    return For(initial=p[2], condition=p[4], increment=p[6], body=p[9])