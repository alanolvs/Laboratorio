import pytest
import unittest

''''Função 1'''
from main import calcular_desconto

def test_desconto_10_porcento():
    resultado = calcular_desconto(100, 10)
    assert resultado == 90

def test_sem_desconto():
    resultado = calcular_desconto(100, 0)
    assert resultado == 100

def test_desconto_total():
    resultado = calcular_desconto(100, 100)
    assert resultado == 0

def test_cupom_invalido():
    with pytest.raises(ValueError):
        calcular_desconto(100, 150)

'''Função 2'''
from main import adicionar_ao_estoque

#Caminho Feliz: Testa a adição de um produto válido
def test_produto_novo(): 
    estoque = {}
    adicionar_ao_estoque(estoque, "RTX 9090 TI SUPER", 20)
    assert estoque["RTX 9090 TI SUPER"] == 20
    
#Tratamento de Exceção: Testa se o erro é gerado com quantidade negativa
def test_quantidade_negativa():
    estoque = {}
    with pytest.raises(ValueError):
        adicionar_ao_estoque(estoque, "PS9 PRO MAX", -10)

'''Função 3'''
from main import verificar_disponibilidade

class TestGerenciamentoEstoque(unittest.TestCase):

    def setUp(self):
   
        self.estoque_padrao = {
            "notebook": 10, 
            "mouse": 50,
            "teclado": 0
        }

    def test_caminho_feliz_estoque_suficiente(self):
        produto = "notebook"
        quantidade = 2
        
        resultado = verificar_disponibilidade(self.estoque_padrao, produto, quantidade)
        
        self.assertTrue(resultado, "Deveria retornar True para um pedido menor que o estoque.")

    def test_estoque_insuficiente_deve_retornar_falso(self):
        produto = "notebook"
        quantidade = 15 
        
        resultado = verificar_disponibilidade(self.estoque_padrao, produto, quantidade)
        
        self.assertFalse(resultado, "Deveria retornar False pois o pedido (15) é maior que o estoque (10).")

    def test_produto_inexistente_deve_retornar_falso(self):
        produto = "monitor" #Não está no estoque_padrao
        quantidade = 1
        
        resultado = verificar_disponibilidade(self.estoque_padrao, produto, quantidade)
        
        self.assertFalse(resultado, "Deveria retornar False para um produto que não existe no catálogo.")

    def test_pedido_exato_ao_estoque(self):
        produto = "mouse"
        quantidade = 50
        
        resultado = verificar_disponibilidade(self.estoque_padrao, produto, quantidade)
        
        self.assertTrue(resultado, "Deveria retornar True quando o pedido é exatamente igual ao estoque.")

if __name__ == '__main__':
    unittest.main()
    
'''Função 4'''
from main import validar_cep

def test_validar_cep():
    assert validar_cep(48000178) == True
    assert validar_cep("48000178") == True
    assert validar_cep("48000-178") == True
    assert validar_cep(490009343434179) == False

'''Função 5'''
from main import calcular_frete

#Teste do ValueError
def test_valores_invalidos():
    with pytest.raises(ValueError):
        calcular_frete(-10, 2)

#Teste do peso
def test_peso_ate_1():
    assert calcular_frete(50, 1.0) == 10
def test_peso_entre_1_e_5():
    assert calcular_frete(50, 3.0) == 18
def test_peso_acima_5():
    assert calcular_frete(50, 6.0) == 30

#Testes de distância
def test_distancia_ate_100():
    assert calcular_frete(100, 1.0) == 10
def test_distancia_acima_100():
    assert calcular_frete(150, 1.0) == 12.5

#Testes combinados
def test_peso_e_distancia():
    # 18 + (0.05 * 50) = 20.5
    assert calcular_frete(150, 3.0) == 20.5

#Testes de limites
def test_limite_peso_1():
    assert calcular_frete(100, 1.0) == 10
def test_limite_peso_5():
    assert calcular_frete(100, 5.0) == 18
def test_distancia_exatamente_100():
    assert calcular_frete(100, 6.0) == 30

#Caso maior
def test_distancia_grande():
    # 30 + (0.05 * 900) = 75
    assert calcular_frete(1000, 6.0) == 75

'''Função 6'''
from main import remover_item_carrinho

def test_remover_item():
    carrinho = [{'nome': 'Labubu'}, {'nome': 'Caderno'}]
    
    resultado = remover_item_carrinho(carrinho, 'Labubu')
    
    assert resultado == [{'nome': 'Caderno'}]

'''Função 7'''
from main import aplicar_taxa
def test_sem_taxa():
    assert aplicar_taxa(100, 2) == 100

def test_taxa_5_limite():
    assert aplicar_taxa(100, 3) == 105

def test_taxa_5_porcento():
    assert aplicar_taxa(100, 5) == 105

def test_taxa_10_porcento():
    assert aplicar_taxa(100, 10) == 110

def test_parcelas_invalidas():
    with pytest.raises(ValueError):
        aplicar_taxa(100,0)