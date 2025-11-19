from CodigoProyecto import CoefiA as CA
import math

def test_CoefiA():
    CoeficienteA = CA.main()
    assert math.isclose(CoeficienteA, 1.0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"
    
