def calcular_desconto(valor, cupom):
    if cupom < 0 or cupom > 100:
        raise ValueError("Cupom inválido")

    valor_de_desconto = valor * cupom / 100
    return valor - valor_de_desconto
    calcular_desconto(100, 150)