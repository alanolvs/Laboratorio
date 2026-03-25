from app.ecommerce import calcular_desconto
import pytest

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