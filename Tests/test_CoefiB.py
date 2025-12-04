from CodigoProyecto import CoefiB as CB
import math

def test_CoefiB1TX():
    CoefB = CB.main1TX()
    assert math.isclose(CoefB, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoefB}"
    
def test_CoefiB1VX():
    CoefB = CB.main1VX()
    assert math.isclose(CoefB, 1), f"La prueba falló. Esperado: 1.0, Obtenido: {CoefB}"
    
def test_CoefiB2TX():
    CoefB = CB.main2TX()
    assert math.isclose(CoefB, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoefB}"
    
def test_CoefiB2VX():
    CoefB = CB.main2VX()
    assert math.isclose(CoefB, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoefB}"

def test_CoefiB3TX():
    CoefB = CB.main3TX()
    assert math.isclose(CoefB, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoefB}"
    
def test_CoefiB3VX():
    CoefB = CB.main3VX()
    assert math.isclose(CoefB, -1), f"La prueba falló. Esperado: 1.0, Obtenido: {CoefB}"
    
def test_CoefiB4TX():
    CoefB = CB.main4TX()
    assert math.isclose(CoefB, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoefB}"
    
def test_CoefiB4VX():
    CoefB = CB.main4VX()
    assert math.isclose(CoefB, -2), f"La prueba falló. Esperado: 1.0, Obtenido: {CoefB}"
    
def test_CoefiB5TX():
    CoefB = CB.main5TX()
    assert math.isclose(CoefB, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoefB}"
    
def test_CoefiB5VX():
    CoefB = CB.main5VX()
    assert math.isclose(CoefB, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoefB}"
    
def test_CoefiB6TX():
    CoefB = CB.main6TX()
    assert math.isclose(CoefB, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoefB}"
    
def test_CoefiB6VX():
    CoefB = CB.main6VX()
    assert math.isclose(CoefB, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoefB}"
