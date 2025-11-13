import unittest
import sys
import os

# Agrega la carpeta CodigoProyecto al path para que Python la pueda encontrar como paquete
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importamos las funciones refactorizadas del paquete CodigoProyecto
try:
    from CodigoProyecto.CalculosMetodos import TablaXyT, TablaXyV
except ImportError as e:
    # Esto ocurre si falta el archivo __init__.py en CodigoProyecto/
    print(f"Error de Importación: {e}. Asegúrate de tener un archivo __init__.py en la carpeta CodigoProyecto/")
    raise

class TestCalculosMetodos(unittest.TestCase):

    # Método auxiliar para comparar listas de floats con tolerancia
    def _assert_lists_almost_equal(self, list1, list2, places=5, msg=None):
        self.assertEqual(len(list1), len(list2), "Las listas tienen diferente longitud.")
        for a, b in zip(list1, list2):
            self.assertAlmostEqual(a, b, places=places, msg=msg)

    def test_transformacion_tabla1(self):
        print("--- Ejecutando Prueba: Tabla 1 ---")
        # Datos de entrada (tomados de mainTabla1)
        tabla_x = [1.000 , 0.951 , 0.809 , 0.588 , 0.309 , 0.000]
        tabla_t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
        tabla_v = [0.000 , -0.485 , -0.923 , -1.271 , -1.491 , -1.571]

        # Resultados esperados (calculados: T^2, X^2, V^2)
        esperado_t_sq = [0.000, 0.040, 0.160, 0.360, 0.640, 1.000]
        
        # X^2 (usando tabla_x)
        esperado_x_sq = [1.000000, 0.904401, 0.654481, 0.345744, 0.095481, 0.000000] 
        # V^2 (usando tabla_v, los negativos se vuelven positivos al cuadrado)
        esperado_v_sq = [0.000000, 0.235225, 0.851929, 1.615441, 2.223081, 2.468041]

        try:
            # Prueba T^2
            resultado_t_sq = TablaXyT(tabla_x, tabla_t)
            self._assert_lists_almost_equal(resultado_t_sq, esperado_t_sq, places=5, msg="MAL: Error en el cálculo de T^2.")
            print("OK! Tabla 1 (T^2) calculada correctamente.")

            # Prueba X^2 y V^2
            resultado_x_sq, resultado_v_sq = TablaXyV(tabla_x, tabla_v)
            self._assert_lists_almost_equal(resultado_x_sq, esperado_x_sq, places=5, msg="MAL: Error en el cálculo de X^2.")
            self._assert_lists_almost_equal(resultado_v_sq, esperado_v_sq, places=5, msg="MAL: Error en el cálculo de V^2.")
            print("OK! Tabla 1 (X^2 y V^2) calculada correctamente.")

        except AssertionError as e:
            # Imprime el mensaje de error de la aserción
            print(f"FALLO: {e}")
            raise # Lanza la excepción para que unittest la reporte como fallo

# Si deseas agregar más pruebas, puedes seguir el mismo patrón para mainTabla2, mainTabla3, etc.

if __name__ == '__main__':
    unittest.main()