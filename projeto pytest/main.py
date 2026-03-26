'''Função 1'''
def calcular_desconto(valor, cupom):
    if cupom < 0 or cupom > 100:
        raise ValueError("Cupom inválido")

    valor_de_desconto = valor * cupom / 100
    return valor - valor_de_desconto
    calcular_desconto(100, 150)
    
'''Função 2'''
def adicionar_ao_estoque(estoque, produto, quantidade):
    """Adiciona um novo produto ou atualiza a quantidade de um existente no estoque."""
    if quantidade <= 0:
        raise ValueError("Erro: A quantidade precisa ser positiva.")
    
    if produto in estoque:
        estoque[produto] += quantidade

    else:
        estoque[produto] = quantidade
        
    return estoque

'''Função 3'''
def verificar_disponibilidade(estoque, produto, quantidade):
    if produto in estoque and estoque[produto] >= quantidade:
        return True
    
    return False

'''Função 4'''
def validar_cep(cep): 
    formattedCep = str(cep).replace("-", "")

    if len(formattedCep) == 8:
        return True
    
    else:
        return False

'''Função 5'''
def calcular_frete(distancia, peso):
    """
    calcula o valor de frete com base na distancia percorrida e o peso

    Args:
        distancia(int,float): distancia percorrida pelo frete
        peso(int, float): peso da carga

    Returns:
        taxa(int,float): valor a ser pago pelo frete da carga

    Raises:
        ValueError: se algum dos valores for negativo
    """
    taxa = 0
    if distancia < 0 or peso < 0:
        raise ValueError("Distância e peso não podem ser negativos")
    if peso <=1.0:
        taxa += 10
    if peso > 1.0 and peso <=5.0:
        taxa += 18
    if peso > 5.0:
        taxa += 30
    if distancia >100:
        taxa += 0.05 *(distancia - 100)
    
    return taxa

'''Função 6'''
def remover_item_carrinho(carrinho, nome_item):
    carrinho_atualizado = []
    
    for item in carrinho:
        if item['nome'] != nome_item:
            carrinho_atualizado.append(item)
            
    return carrinho_atualizado

'''Função 7'''
def aplicar_taxa (valor, parcelas):
    if parcelas <=0:
        raise ValueError("Número de parecelas invalidas")
    if parcelas <=2:
        taxa = 0
    elif parcelas <=5 :
        taxa = 0.05
    else:
        taxa = 0.10
    valor_final = valor * (1 + taxa)
    return round(valor_final, 2)