from CodigoProyecto import CoefiB as CB
import math

def test_CoefiB():
    CoefB = CB.main()
    assert math.isclose(CoefB, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoefB}"