
@pg.production('comando : decfor PONTOEVIRGULA')


@pg.production('decfor : FOR ABREPARENTESES expr PONTOEVIRGULA operacao PONTOEVIRGULA decatrib FECHAPARENTESES INICIOBLOCO listacomando FIMBLOCO')
def for_loop(self, p):
    return For(initial=p[2], condition=p[4], increment=p[6], body=p[9])