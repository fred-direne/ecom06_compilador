@self.pg.production('program : listacomando')
def program_function(self, p):
    return p[0]

@pg.production('decvar : INT IDENT PONTOEVIRGULA')
@pg.production('decvar : FLOAT IDENT PONTOEVIRGULA')
@pg.production('decvar : CHAR IDENT PONTOEVIRGULA')
def declare_int(self, p):
    return Variable

@pg.production('comando : decvar PONTOEVIRGULA')
@pg.production('comando : decatrib PONTOEVIRGULA')
@pg.production('comando : decprint PONTOEVIRGULA')
@pg.production('comando : decread PONTOEVIRGULA')
@pg.production('comando : decif PONTOEVIRGULA')
@pg.production('comando : decfor PONTOEVIRGULA')
@pg.production('comando : decwhile PONTOEVIRGULA')
def statement_list_return(self, p):
    return p[0]

@pg.production('listacomando : comando')
def statement_list_statement(self, p):
    return NodeList([p[0]])

@pg.production('listacomando : comando listacomando')
def statement_list_statement(self, p):
    st = NodeList([p[0]])
    st.extend(p[1].get_items())
    return st

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

@pg.production('decread : READ ABREPARENTESES IDENT FECHAPARENTESES PONTOEVIRGULA')

@pg.production('decprint : PRINT ABREPARENTESES operacao FECHAPARENTESES PONTOEVIRGULA')

@pg.production('decatrib : INT IDENT ATRIBUICAO NUMERO PONTOEVIRGULA')
@pg.production('decatrib : INT IDENT ATRIBUICAO IDENT PONTOEVIRGULA')
@pg.production('decatrib : FLOAT IDENT ATRIBUICAO REAL PONTOEVIRGULA')
@pg.production('decatrib : FLOAT IDENT ATRIBUICAO IDENT PONTOEVIRGULA')
@pg.production('decatrib : CHAR IDENT ATRIBUICAO IDENT PONTOEVIRGULA')
def atrib(self, p):
    return Assignment(left=Variable(p[1].getstr()), right=p[3])

@pg.production('decatrib : CHAR IDENT ATRIBUICAO FECHAASPAS CARACTER ABREASPAS IDENT PONTOEVIRGULA')
def atrib(self, p):
    return Assignment(left=Variable(p[1].getstr()), right=p[6])


@pg.production('expr  : expr SOMA expr PONTOEVIRGULA')
@pg.production('expr  : expr SUBTRACAO expr PONTOEVIRGULA')
@pg.production('expr  : expr MULTIPLICACAO expr PONTOEVIRGULA')
@pg.production('expr  : expr DIVISAO expr PONTOEVIRGULA')
@pg.production('expr  : expr RESTO expr PONTOEVIRGULA')
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