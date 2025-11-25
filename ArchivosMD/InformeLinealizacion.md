# INFORME 
Linealizacion de datos

## INTEGRANTES
Moral Melgar Sebastian Erol - CodSis:202503006
###
Leandro Andre Ortuno Cespedes - Codsis:202507179
###
Ventura Guzman Jose Ignacio - CodSis:202505851

## DATOS 
Como datos tenemos las 6 tablas las cuales fueron proporcionadas por el Ing.Grabriel, las cuales como tienen 3 variables(t,x,v), t = tiempo, x = posicion y 
v = velocidad, que seran distribuidas de la siguiente manera: una tabla solo tendra las variables t y x, la otra tendra las variables v y x, con el objetivo que
sean tablas planas con solo dos ejes de coordenadas(X y Y):

TABLA 1:
	tabla1x = [1.000 , 0.951 , 0.809 , 0.588 , 0.309 , 0.000]
	tabla1t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	tabla1v = [0.000 , -0.485 , -0.923 , -1.271 , -1.491 , -1.571]

TABLA 2:
	tabla2x = [0.707 , 0.410 , 0.060 , -0.298 , -0.618, -0.856]
	tabla2t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	tabla2v = [-1.283 , -1.654 , -1.811 , -1.731 , -1.427 , -0.936]


TABLA 3:
	tabla3x = [0.0 , 0.710 , 1.327 , 1.772 , 1.986 , 1.941]
	tabla3t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	tabla3v = [3.628 , 3.392, 2.714, 1.683 , 0.483 , -0.873]


TABLA 4:
	tabla4x = [0.0 , 0.860 , 1.552, 1.944 , 1.958, 1.591]
	tabla4t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	tabla4v = [4.443, 4.012, 2.801, 1.047, -0.910, -2.691]


TABLA 5:
	tabla5x = [2.000 , 1.806 , 1.261 , 0.471 , -0.410 , -1.211]
	tabla5t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	tabla5v = [0.0 , -1.910 , -3.448 , -4.318 , -4.349 , -3.535]

TABLA 6:
	tabla6x = [-1.000 , -0.809 , -0.309 , 0.309 , 0.809 , 1.000]
	tabla6t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	tabla6v = [0.000 , 1.847 , 2.988 , 2.988 , 1.847 , 0.000]
	

## CODIGO

### CODIGO DE LINEALIZACION
import math
//Parte de la tarea para el informe:
//poetry run python -m CodigoProyecto.GenerarGrafico Csv/tabla1.csv

//En Tabla XyT
def TablaXyT(tabla, tabla2):
    tablauxXyT = []
    aux = 0
    for t in range(0,len(tabla2),1):
        aux = math.pow(tabla2[t], 2)
        tablauxXyT.append(aux)
    return tablauxXyT 
    
//En Tabla XyV
def TablaXyV(tabla, tabla2):
    tablauxXyV = []
    tablauxXyV2 = []
    aux = 0
    for x in range(0,len(tabla),1):
        aux = math.pow(tabla[x], 2)
        tablauxXyV.append(aux)
    for v in range(0,len(tabla2),1):
        aux = math.pow(tabla2[v],2)
        tablauxXyV2.append(aux)
    return tablauxXyV, tablauxXyV2 



//no olvidar guardar los datos en un archivo cvs


//METODOS MAIN: 
//main Tabla 1
def mainTabla1():
	#lista de datos del  Tabla1(t y x)
	tabla1x = [1.000 , 0.951 , 0.809 , 0.588 , 0.309 , 0.000]
	tabla1t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	#lista de datos del  Tabla1(v y x) es
	tabla1x = [1.000 , 0.951 , 0.809 , 0.588 , 0.309 , 0.000]
	tabla1v = [0.000 , -0.485 , -0.923 , -1.271 , -1.491 , -1.571]
	#metodo cambbio de variable XyT:
	TablaXyT(tabla1x, tabla1t)
	#metodo cambbio de variable XyV:
	TablaXyV(tabla1x, tabla1v)

//main Tabla 2
def mainTabla2():
	# lista de datos de los tabla2(t y x) es
	tabla2x = [0.707 , 0.410 , 0.060 , -0.298 , -0.618, -0.856]
	tabla2t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	# lista de datos de los tabla2(v y x) es
	tabla2x = [0.707 , 0.410 , 0.060 , -0.298 , -0.618, -0.856]
	tabla2v = [-1.283 , -1.654 , -1.811 , -1.731 , -1.427 , -0.936]
	
	#metodo cambbio de variable XyT:
	TablaXyT(tabla2x, tabla2t)
	#metodo cambbio de variable XyV:
	TablaXyV(tabla2x, tabla2v)


//main Tabla 3
def mainTabla3():
	#lista de datos de la Tabla3(t y x) es
	tabla3x = [0.0 , 0.710 , 1.327 , 1.772 , 1.986 , 1.941]
	tabla3t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	# lista de datos de los tabla3(v y x) es
	tabla3x = [0.0 , 0.710 , 1.327 , 1.772 , 1.986 , 1.941]
	tabla3v = [3.628 , 3.392, 2.714, 1.683 , 0.483 , -0.873]
	
	#metodo cambbio de variable XyT:
	TablaXyT(tabla3x, tabla3t)
	#metodo cambbio de variable XyV:
	TablaXyV(tabla3x, tabla3v)


//main Tabla 4
def mainTabla4():
	#lista de datos del tabla4(t y x) es
	tabla4x = [0.0 , 0.860 , 1.552, 1.944 , 1.958, 1.591]
	tabla4t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	#lista de datos del tabla4(v y x) es
	tabla4x = [0.0 , 0.860 , 1.552, 1.944 , 1.958, 1.591]
	tabla4v = [4.443, 4.012, 2.801, 1.047, -0.910, -2.691]
	#metodo cambbio de variable XyT:
	TablaXyT(tabla4x, tabla4t)
	#metodo cambbio de variable XyV:
	TablaXyV(tabla4x, tabla4v)


//main Tabla 5
def mainTabla5(): 
	#lista de datos del tabla5(t y x) es
	tabla5x = [2.000 , 1.806 , 1.261 , 0.471 , -0.410 , -1.211]
	tabla5t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	#lista de datos del tabla5(v y x) es
	tabla5x = [2.000 , 1.806 , 1.261 , 0.471 , -0.410 , -1.211]
	tabla5v = [0.0 , -1.910 , -3.448 , -4.318 , -4.349 , -3.535]
	
	#metodo cambbio de variable XyT:
	TablaXyT(tabla5x, tabla5t)
	#metodo cambbio de variable XyV:
	TablaXyV(tabla5x, tabla5v)


//main Tabla 6
def mainTabla6():
	#lista de datos del tabla6(t y x) es
	tabla6x = [-1.000 , -0.809 , -0.309 , 0.309 , 0.809 , 1.000]
	tabla6t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	#lista de datos del tabla6(v y x) es
	tabla6x = [-1.000 , -0.809 , -0.309 , 0.309 , 0.809 , 1.000]
	tabla6v = [0.000 , 1.847 , 2.988 , 2.988 , 1.847 , 0.000]
	
	#metodo cambbio de variable XyT:
	TablaXyT(tabla6x, tabla6t)
	#metodo cambbio de variable XyV:
	TablaXyV(tabla6x, tabla6v)
	
//MAIN: para todas las funciones:
def main():
    print("TABLA1")
    print(mainTabla1())
    print("TABLA2")
    print(mainTabla2())
    print("TABLA3")
    print(mainTabla3())
    print("TABLA4")
    print(mainTabla4())
    print("TABLA5")
    print(mainTabla5())
    print("TABLA6")
    print(mainTabla6())
    
if __name__ == "__main__":
    main()
        
    

### CODIGO CALCULO COEFICIENTE A
import math


def sumx(listaX):
    Sumx = 0
    for i in range(0, len(listaX), 1):
        Sumx += listaX[i]
    return Sumx

def sumx2(listaX):
    Sumx2 = 0
    for i in range(0, len(listaX), 1):
        Sumx2 += math.pow(listaX[i], 2)
    return Sumx2
    
def sumy(listaY):
    Sumy = 0
    for i in range(0, len(listaY), 1):
        Sumy += listaY[i]
    return Sumy

def sumxy(listaX, listaY):
    Sumxy = 0
    for i in range(0, len(listaX), 1):
        Sumxy += listaX[i] * listaY[i]
    return Sumxy

def delta(n, Sumx, Sumx2):
    Delta = 0
    Delta = (n * Sumx2) - math.pow(Sumx, 2)
    return Delta

def CoeficienteA(Sumx, Sumx2, Sumy, Sumxy, Delta):
    return (Sumy * Sumx2 - Sumxy * Sumx)/Delta

def main():
    #listas de prueba:
	tabla1x = [1.000 , 0.951 , 0.809 , 0.588 , 0.309 , 0.000]
	tabla1t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	#Todas las listas proporcionadas por el Ing.Gabriel son de tamaño 6
	n = len(tabla1x)
	Sumx = sumx(tabla1x)
	Sumx2 = sumx2(tabla1x)
	Sumy = sumy(tabla1t)
	Sumxy = sumxy(tabla1x, tabla1t)
	Delta = delta(n, Sumx, Sumx2)
	CofA = (int)(CoeficienteA(Sumx, Sumx2,  Sumy, Sumxy, Delta))
	return CofA



if __name__ == "__main__":
    main()

### CODIGO CALCULO COEFICIENTE B
import math

def suma_x(listaX):
    Suma_x = 0
    for i in range(0, len(listaX), 1):
       Suma_x += listaX[i]
    return Suma_x


def suma_x2(listaX):
    Suma_x2 = 0
    for i in range(0, len(listaX), 1):
        Suma_x2 += math.pow(listaX[i], 2)
    return Suma_x2


def suma_y(listaY):
    Suma_y = 0
    for i in range(0, len(listaY), 1):
        Suma_y += listaY[i]
    return Suma_y


def suma_xy(listaX, listaY):
    Suma_xy = 0
    for i in range(0, len(listaX), 1):
        Suma_xy += listaX[i] * listaY[i]
    return Suma_xy


def delta(n, Suma_x, Suma_x2):
    Delta = 0
    Delta = (n * Suma_x2) - math.pow(Suma_x, 2)
    return Delta


def CoefB(n, Suma_x, Suma_x2, Suma_y, Suma_xy, Delta):
    return (n * Suma_xy - Suma_x * Suma_y) / Delta


def main():
    tabla1x = [1.000 , 0.951 , 0.809 , 0.588 , 0.309 , 0.000]
    
    tabla1t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]

    n = len(tabla1x)

    Suma_x = suma_x(tabla1x)

    Suma_x2 = suma_x2(tabla1x)

    Suma_y = suma_y(tabla1t)

    Suma_xy = suma_xy(tabla1x, tabla1t)

    Delta = delta(n, Suma_x, Suma_x2)

    CofB = (int)(CoefB(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))

    return CofB


if __name__ == "__main__":

    main()	

### TEST CALCULO COEFICIENTE A
from CodigoProyecto import CoefiA as CA
import math

def test_CoefiA():
    CoeficienteA = CA.main()
    assert math.isclose(CoeficienteA, 1.0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"
    


### TEST CALCULO COEFICIENTE B
from CodigoProyecto import CoefiB as CB

import math

def test_CoefiB():
    CoefB = CB.main()
    assert math.isclose(CoefB, 1.0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoefB}"

## COMO USAR CODIGO

### USO CODIGO CALCULO LINEALIZACION


### USO CODIGO CALCULO COEFICIENTE A

### USO CODIGO CALCULO COEFICIENTE B


### USO DE LOS TESTS
Primreo se importa en la parte superior el archivo de donde usaremos la importacion para el respectivo calculo con los test
de la siguiente manera:

        from CalculoProyecto import CoefiA as CA
importamos la carpeta, el archivo y le designamos un alias, el alias nos servira para poder usar los metodos que devuelven los resultados esperados,
una vez realizado esto, en la terminal se pone el comando de pytest para que haga  los respectivos calculos de los test.

Mismo caso para lo que es el para el coeficiente de B y para los errores
se importe la carpeta, el archivo y se le designa un alias.


## RESULTADOS
### RESULTADOS LINEALIZACION
Los resultados esperados en esta seccion de repositorio son las tablas linealizadas, posteriormente, en la carpeta de GraficosPoetry, estan todas las imagenes de las 
tablas, T y X e V y X, ambas sin cambio y con cambio.


### RESULTADOS COEFICIENTES A Y B


### RESULTADOS TESTS
Los resultados de los test tienen que que haya pasado los test, como resultado obtenemos que no tenemos errores en el resultado de los test
![Foto de el resultado de los test mediante la terminal](pytestCoefi.png)

## OBSERVACIONES
Para realizar el cambio de variable apropiado, luego de resolver con el metodo de movimiento armonico simple, viendo que en las tablas tenemos valores de 0 o 
negativos, se opto por usar el metodo de elevacion de datos al cuadrado, ya que es el mas apropiado para el tipo de  datos que manejamos con las tablas.
