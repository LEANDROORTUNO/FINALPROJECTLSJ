from CodigoProyecto import calc_errores as CE
import math
 
def test_errorA () : # compare el resultado de solo el mainA con el reultado esperado
        CoeA= (int)(CE.main_errorA())
        assert math.isclose(CoeA,1), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeA}"

def test_errorB() : # compare el resultado de solo el mainA con el reultado esperado
         CoeB = (int)(CE.main_errorB())
         assert math.isclose(CoeB,1), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeB}"