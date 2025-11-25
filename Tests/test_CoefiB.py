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