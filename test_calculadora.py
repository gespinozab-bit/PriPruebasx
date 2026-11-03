import pytest

from calculadora import sumar, restar, multiplicar, division

def test_sumar(): 
    assert sumar(2, 3) == 5 
    assert sumar(-1, 1) == 0 
    assert sumar(0, 0) == 0 
    assert sumar(-5, -3) == -8 
    assert sumar(2.5, 3.5) == 6.0
    
def test_restar(): 
    assert restar(5, 3) == 2 
    assert restar(-1, -1) == 0 
    assert restar(0, 0) == 0 
    assert restar(-5, -3) == -2 
    assert restar(2.5, 1.5) == 1.0

def test_multiplicar(): 
    assert multiplicar(2, 3) == 6 
    assert multiplicar(-1, 1) == -1 
    assert multiplicar(0, 5) == 0 
    assert multiplicar(-5, -3) == 15 
    assert multiplicar(2.5, 4) == 10.0
    
def test_division(): 
    assert division(6, 3) == 2 
    assert division(-4, 2) == -2 
    assert division(0, 5) == 0 
    assert division(-9, -3) == 3 
    assert division(7.5, 2.5) == 3.0
    

def test_division_por_cero():
    with pytest.raises(ZeroDivisionError):
        division(5, 0)
    
    
    
    
