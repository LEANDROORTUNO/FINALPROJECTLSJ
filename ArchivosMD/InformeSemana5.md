# INFORME SEMANA 5
Informe de la Semana 5
## INTEGRANTES
Morant Melgar Sebastian Erol - CodSis: 202503006
###
Ortuno Cespedes Leandro Andre - CodSis: 202507179
###
Ventura Guman Jose Ignacio - CodSis 202505851

## PARTE JOSE-DATOS

COEFIS B :

CoefiB1TX
CoefiB1VX
CoefiB2TX
CoefiB2VX
CoefiB3TX
CoefiB3VX
CoefiB4TX
CoefiB4VX
CoefiB5TX
CoefiB5VX
CoefiB6TX
CoefiB6VX

MASAS:
 
Tabla1 = masa:4 
Tabla2 = masa:3
Tabla3 = masa:3
Tabla4 = masa:2
Tabla5 = masa:2
Tabla6 = masa:1

## CODIGO

import CoefiB as ctte
import math

def k_tabla1TX():
    CoefiB1TX = ctte.main1TX()
    k = 4 * (-CoefiB1TX)
    return k
   
def k_tabla1VX():
    CoefiB1VX = ctte.main1VX()
    k = 4 * (-CoefiB1VX)
    return k
        
def k_tabla2TX():
    CoefiB2TX = ctte.main2TX()
    k = 3 * (-CoefiB2TX)
    return k
    
def k_tabla2VX():
    CoefiB2VX = ctte.main2VX()
    k = 3 * (-CoefiB2VX)
    return k
    
def k_tabla3TX():
    CoefiB3TX = ctte.main3TX()
    k = 3 * (-CoefiB3TX)
    return k

def k_tabla3VX():
    CoefiB3VX = ctte.main3VX()
    k = 3 * (-CoefiB3VX)
    return k

def k_tabla4TX():
    CoefiB4TX = ctte.main4TX()
    k = 2 * (-CoefiB4TX)
    return k

def k_tabla4VX():
    CoefiB4VX = ctte.main4VX()
    k = 2 * (-CoefiB4VX)
    return k

def k_tabla5TX():
    CoefiB5TX = ctte.main5TX()
    k = 3 * (-CoefiB5TX)
    return k

def k_tabla5VX():
    CoefiB5VX = ctte.main5VX()
    k = 3 * (-CoefiB5VX)
    return k

def k_tabla6TX():
    CoefiB6TX = ctte.main6TX()
    k = 1 * (-CoefiB6TX)
    return k

def k_tabla6VX():
    CoefiB6VX = ctte.main6VX()
    k = 1 * (-CoefiB6VX)
    return k

def promedio_k_tabla1():
    k1TX = k_tabla1TX()
    k1VX = k_tabla1VX()
    promedio = (k1TX + k1VX) / 2
    return promedio

def promedio_k_tabla2():
    k2TX = k_tabla2TX()
    k2VX = k_tabla2VX()
    promedio = (k2TX + k2VX) / 2
    return promedio

def promedio_k_tabla3():
    k3TX = k_tabla3TX()
    k3VX = k_tabla3VX()
    promedio = (k3TX + k3VX) / 2
    return promedio

def promedio_k_tabla4():
    k4TX = k_tabla4TX()
    k4VX = k_tabla4VX()
    promedio = (k4TX + k4VX) / 2
    return promedio

def promedio_k_tabla5():
    k5TX = k_tabla5TX()
    k5VX = k_tabla5VX()
    promedio = (k5TX + k5VX) / 2
    return promedio

def promedio_k_tabla6():
    k6TX = k_tabla6TX()
    k6VX = k_tabla6VX()
    promedio = (k6TX + k6VX) / 2
    return promedio

def main():
    promedio1 = promedio_k_tabla1()
    promedio2 = promedio_k_tabla2()
    promedio3 = promedio_k_tabla3()
    promedio4 = promedio_k_tabla4()
    promedio5 = promedio_k_tabla5()
    promedio6 = promedio_k_tabla6()
    promedio_general = (promedio1 + promedio2 + promedio3 + promedio4 + promedio5 + promedio6) / 6
    return promedio_general

## COMO USAR CODIGO

Este codigo tiene la funcion de sacar las constantes elasticas de cada tabla, como la constante k 
es: k = m * (-B), pues lo que hice fue sacar la constante de cada tabla.
Para que esto funcione lo primero que se tiene que hacer es importar los datos del coeficiente B 
de cada tabla TX y VX de otro archivo para asi utilizar esos datos y realizar las operaciones, 
despues de sacar las constantes de cada tabla procedemos a sacar el promedio de todas las 
constantes de las tablas, sumando y dividiendolo entre 6 ya que son 6 tablas, asi es como saque 
la constante k general de todas las tablas.

## RESULTADOS

El resultado es:
k = 0.25

## OBSERVACIONES

El codigo fue sencillo en pocas palabras ya que simplemente utilice los datos que ya habian en 
otro codigo que en este caso fue coefB, despues ya solo fue colocar las masas de cada tabla ya
dadas y asi realizar las operaciones. 

## PARTE SEBAS-DATOS

k = 0.25
m = 9
error de la masa = 01

## CODIGO
import math
import Constante_k as ctte
def periodoT():
        k = ctte.main()
        m = 9
        return 2*math.pi*math.sqrt(m/k)
def error_periodoT():
        m = 9
        dm = 0.1
        return (periodoT()/(2*m)) *dm

## COMO USAR CODIGO
El codigo sirve para hallar el periodo de oscilacion (T) junto con su error del periodo.
En primer lugar hay que dirigirse a la consola del programa donde hay llamarla por su funcion
(periodoT()) y el return devolvera el resultado el cual es el periodo de oscilacion.
Tambien se procede con el error tambien llamandola por su funcion (error_periodoT()),la cual
nos devolvera su resultado.

## RESULTADOS
periodoT = 37.69911184307752
error_periodoT = 0.20943951023931953

## OBSERVACIONES
El codigo es corto pero muy funcional siempre hay que compilarlo para suelte los resultados.



## PARTE LEANDRO-DATOS

## CODIGO
from pathlib import Path
from typing import Tuple, Dict, Any # Importamos Dict y Any para el tipado
import matplotlib.pyplot as plt
import numpy as np
import PeriodoT as PT
import Constante_k as CK
import CoefiA as CA
//poetry run python CodigoProyecto/GraficaMovArmonico.py

def generate_mas_data(A: float, k: float, m: float, t_max: float) -> Dict[str, Any]:
    """
    Genera y devuelve los datos del M.A.S. en un diccionario.
    """
    omega = np.sqrt(k / m)
    t = np.linspace(0, t_max, 500)
    x = A * np.cos(omega * t) 
    
    # Devolvemos un diccionario con las claves necesarias
    data = {
        't': t,
        'x': x,
        'tName': "Tiempo (s)",
        'xName': "Posición (m)",
        'm': m, # Agregamos la masa para el título
        'k': k  # Agregamos k para el título
    }
    
    return data

def make_plot(data: Dict[str, Any]) -> Tuple[plt.Figure, plt.Axes]:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data['t'], data['x'], marker=None, color='red', linewidth=2)
    
    ax.set_title(f"Movimiento Armónico Simple (M={data['m']:.1f}kg, K={data['k']:.1f}N/m)", fontsize=14)
    ax.set_xlabel(data['tName'], fontsize=12)
    ax.set_ylabel(data['xName'], fontsize=12)
    
    ax.axhline(0, color='black', linestyle='-', linewidth=0.8) 
    ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.7)
    
    fig.tight_layout()
    return fig, ax

// --- Las funciones save_plot y main quedan casi iguales ---
def save_plot(fig: plt.Figure, filename: str | Path) -> None:
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(filename, format="png", dpi=150)

// Parámetros del M.A.S.
A = CA.promedio()
k = CK.main()
m = 9.0
T= PT.periodoT()


def main() -> None:
    mas_data = generate_mas_data(A, k, m, T)
    fig, _ = make_plot(mas_data)
    
    output_filename = "GraficosPoetry/GraficoOscilaciones.png"
    save_plot(fig, output_filename)
    
    print(f"✅ Gráfico guardado exitosamente en: {output_filename}")
    
// main
if __name__ == "__main__":
    main()

##COMO USAR CODIGO
Se realizo 3 importaciones para el respectivo codigo, para poder usar los valores de K, T y A, por lo que se realizo lo siguiente: import PeriodoT as PT
import Constante_k as CK
import CoefiA as CA
 en el cual se logro el uso de poetry para graficar la ocsilacion de masa 9m, usando la libreria  numpy y otras herramientas para el correcto uso de poetry:
from pathlib import Path
from typing import Tuple, Dict, Any # Importamos Dict y Any para el tipado
import matplotlib.pyplot as plt
import numpy as np
Se creo un metodo save,plot, para el guardao de la imagen al momento de graficarla con poetry.
se creo metodos de graficacion enfocandonos en la siguiente formula de oscilacion:
x(t)=Acos(ωt)
la cual se uso en el metodo de ocsilacion dentro de codigo, se realizo dos tipos de imagenes, de PRUEBA y con los datos que logramos obtener en el codigo:
los datos de prueba fueron los siguientes: A = 5.0, K = 10.0, m = 9m y para T = 10.0
![Imagen obtenida con los datos de prueba](GraficoOscilacionesPRUEBA.png)
Con los datos que se obtuvo al invocar las funciones correspondientes fueron las siguientes: para A = PT.main(), K = ck.main(), t = PT.promedio() 
![Imagen obtenida con los datos obtenidos por los metodos invocados](GraficoOscilaciones.png)
Una vez teniendo las imagenes vemos que tenemos oscilaciones esperadas con la masa 9m, que es lo que se esperaba dentro de los graficos con poetry

Para lograr obtener el grafico, utilizamos el siguiente comando, dentro de la terminal, para poder obtener la imagen esperada:
poetry run python CodigoProyecto/GraficaMovArmonico.py

El cual una vez ejecutada nos tenia que salir un mensaje de que se creo la imagen correctamente:
print(f"✅ Gráfico guardado exitosamente en: {output_filename}, el cua se guardaba dentro de la carpeta: GraficosPoetry

## RESULTADOS
Los resultados fueron las imagenes con oscialciones, tanto la imagen con los datos de prueba, como la imagen con los datos obtenidos, teniendo asi, graficos
con oscilaciones que es justo lo que se esperaba tener al momento de obtener el codigo.

## OBSERVACIONES
se tuvo que usar dos tipos de datos para poder verificar la eficiencia de el codigo de Grafico de movimiento armonico simple, una vez asegurado que el codigo 
funcionara correctamente se uso los datos obtenidos por los metodos correspondientes,
