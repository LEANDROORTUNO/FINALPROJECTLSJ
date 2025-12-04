from CodigoProyecto import CoefiA as CA
import math

def test_CoefiA1TX():
    CoeficienteA = CA.main1TX()
    assert math.isclose(CoeficienteA, 1), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"
    
def test_CoefiA1VX():
    CoeficienteA = CA.main1VX()
    assert math.isclose(CoeficienteA, -1), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"

def test_CoefiA2TX():
    CoeficienteA = CA.main2TX()
    assert math.isclose(CoeficienteA, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"

def test_CoefiA2VX():
    CoeficienteA = CA.main2VX()
    assert math.isclose(CoeficienteA, -1), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"

def test_CoefiA3TX():
    CoeficienteA = CA.main3TX()
    assert math.isclose(CoeficienteA, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"

def test_CoefiA3VX():
    CoeficienteA = CA.main3VX()
    assert math.isclose(CoeficienteA, 4), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"

def test_CoefiA4TX():
    CoeficienteA = CA.main4TX()
    assert math.isclose(CoeficienteA, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"

def test_CoefiA4VX():
    CoeficienteA = CA.main4VX()
    assert math.isclose(CoeficienteA, 4), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"

def test_CoefiA5TX():
    CoeficienteA = CA.main5TX()
    assert math.isclose(CoeficienteA, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"

def test_CoefiA5VX():
    CoeficienteA = CA.main5VX()
    assert math.isclose(CoeficienteA, -3), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"

def test_CoefiA6TX():
    CoeficienteA = CA.main6TX()
    assert math.isclose(CoeficienteA, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"

def test_CoefiA6VX():
    CoeficienteA = CA.main6VX()
    assert math.isclose(CoeficienteA, 1), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"

