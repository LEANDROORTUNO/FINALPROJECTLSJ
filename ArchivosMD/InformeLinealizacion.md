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


def CoefA(n, Suma_x, Suma_x2, Suma_y, Suma_xy, Delta):
    return (n * Suma_xy - Suma_x * Suma_y) / Delta


// SOLO T y X

def main1TX():
	tabla1t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	tabla1x = [1.000 , 0.951 , 0.809 , 0.588 , 0.309 , 0.000]
	n = len(tabla1x)
	Suma_x = suma_x(tabla1x)
	Suma_x2 = suma_x2(tabla1x)
	Suma_y = suma_y(tabla1t)
	Suma_xy = suma_xy(tabla1x, tabla1t)
	Delta = delta(n, Suma_x, Suma_x2)
	CofA = (int)(CoefA(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))
	return CofA

def main2TX():
	tabla2t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	tabla2x = [0.707 , 0.410 , 0.060 , -0.298 , -0.618, -0.856]
	n = len(tabla2x)
	Suma_x = suma_x(tabla2x)
	Suma_x2 = suma_x2(tabla2x)
	Suma_y = suma_y(tabla2t)
	Suma_xy = suma_xy(tabla2x, tabla2t)
	Delta = delta(n, Suma_x, Suma_x2)
	CofA = (int)(CoefA(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))
	return CofA

def main3TX():
	tabla3t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	tabla3x = [0.0 , 0.710 , 1.327 , 1.772 , 1.986 , 1.941]
	n = len(tabla3x)
	Suma_x = suma_x(tabla3x)
	Suma_x2 = suma_x2(tabla3x)
	Suma_y = suma_y(tabla3t)
	Suma_xy = suma_xy(tabla3x, tabla3t)
	Delta = delta(n, Suma_x, Suma_x2)
	CofA = (int)(CoefA(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))
	return CofA


def main4TX():
	tabla4t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	tabla4x = [0.0 , 0.860 , 1.552, 1.944 , 1.958, 1.591]
	n = len(tabla4x)
	Suma_x = suma_x(tabla4x)
	Suma_x2 = suma_x2(tabla4x)
	Suma_y = suma_y(tabla4t)
	Suma_xy = suma_xy(tabla4x, tabla4t)
	Delta = delta(n, Suma_x, Suma_x2)
	CofA = (int)(CoefA(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))
	return CofA

def main5TX():
	tabla5t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	tabla5x = [2.000 , 1.806 , 1.261 , 0.471 , -0.410 , -1.211]
	n = len(tabla5x)
	Suma_x = suma_x(tabla5x)
	Suma_x2 = suma_x2(tabla5x)
	Suma_y = suma_y(tabla5t)
	Suma_xy = suma_xy(tabla5x, tabla5t)
	Delta = delta(n, Suma_x, Suma_x2)
	CofA = (int)(CoefA(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))
	return CofA

def main6TX():
	tabla6t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	tabla6x = [-1.000 , -0.809 , -0.309 , 0.309 , 0.809 , 1.000]
	n = len(tabla6x)
	Suma_x = suma_x(tabla6x)
	Suma_x2 = suma_x2(tabla6x)
	Suma_y = suma_y(tabla6t)
	Suma_xy = suma_xy(tabla6x, tabla6t)
	Delta = delta(n, Suma_x, Suma_x2)
	CofA = (int)(CoefA(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))
	return CofA



// SOLO V y X
def main1VX():
	tabla1v = [0.000 , -0.485 , -0.923 , -1.271 , -1.491 , -1.571]
	tabla1x = [1.000 , 0.951 , 0.809 , 0.588 , 0.309 , 0.000]
	n = len(tabla1x)
	Suma_x = suma_x(tabla1x)
	Suma_x2 = suma_x2(tabla1x)
	Suma_y = suma_y(tabla1v)
	Suma_xy = suma_xy(tabla1x, tabla1v)
	Delta = delta(n, Suma_x, Suma_x2)
	CofA = (int)(CoefA(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))
	return CofA

def main2VX():
	tabla2v = [-1.283 , -1.654 , -1.811 , -1.731 , -1.427 , -0.936]
	tabla2x = [0.707 , 0.410 , 0.060 , -0.298 , -0.618, -0.856]
	n = len(tabla2x)
	Suma_x = suma_x(tabla2x)
	Suma_x2 = suma_x2(tabla2x)
	Suma_y = suma_y(tabla2v)
	Suma_xy = suma_xy(tabla2x, tabla2v)
	Delta = delta(n, Suma_x, Suma_x2)
	CofA = (int)(CoefA(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))
	return CofA

def main3VX():
	tabla3v = [3.628 , 3.392, 2.714, 1.683 , 0.483 , -0.873]
	tabla3x = [0.0 , 0.710 , 1.327 , 1.772 , 1.986 , 1.941]
	n = len(tabla3x)
	Suma_x = suma_x(tabla3x)
	Suma_x2 = suma_x2(tabla3x)
	Suma_y = suma_y(tabla3v)
	Suma_xy = suma_xy(tabla3x, tabla3v)
	Delta = delta(n, Suma_x, Suma_x2)
	CofA = (int)(CoefA(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))
	return CofA

def main4VX():
	tabla4v = [4.443, 4.012, 2.801, 1.047, -0.910, -2.691]
	tabla4x = [0.0 , 0.860 , 1.552, 1.944 , 1.958, 1.591]
	n = len(tabla4x)
	Suma_x = suma_x(tabla4x)
	Suma_x2 = suma_x2(tabla4x)
	Suma_y = suma_y(tabla4v)
	Suma_xy = suma_xy(tabla4x, tabla4v)
	Delta = delta(n, Suma_x, Suma_x2)
	CofA = (int)(CoefA(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))
	return CofA

def main5VX():
	tabla5v = [0.0 , -1.910 , -3.448 , -4.318 , -4.349 , -3.535]
	tabla5x = [2.000 , 1.806 , 1.261 , 0.471 , -0.410 , -1.211]
	n = len(tabla5x)
	Suma_x = suma_x(tabla5x)
	Suma_x2 = suma_x2(tabla5x)
	Suma_y = suma_y(tabla5v)
	Suma_xy = suma_xy(tabla5x, tabla5v)
	Delta = delta(n, Suma_x, Suma_x2)
	CofA = (int)(CoefA(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))
	return CofA



def main6VX():
	tabla6v = [0.000 , 1.847 , 2.988 , 2.988 , 1.847 , 0.000]
	tabla6x = [-1.000 , -0.809 , -0.309 , 0.309 , 0.809 , 1.000]
	n = len(tabla6x)
	Suma_x = suma_x(tabla6x)
	Suma_x2 = suma_x2(tabla6x)
	Suma_y = suma_y(tabla6v)
	Suma_xy = suma_xy(tabla6x, tabla6v)
	Delta = delta(n, Suma_x, Suma_x2)
	CofA = (int)(CoefA(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))
	return CofA


// main()
def main():
    print("TABLA 1 TX")
    print(main1TX())
    print("TABLA 2 TX")
    print(main2TX())
    print("TABLA 3 TX")
    print(main3TX())
    print("TABLA 4 TX")
    print(main4TX())
    print("TABLA 5 TX")
    print(main5TX())
    print("TABLA 6 TX")
    print(main6TX())
    print("TABLA 1 VX")
    print(main1VX())
    print("TABLA 2 VX")
    print(main2VX())
    print("TABLA 3 VX")
    print(main3VX())
    print("TABLA 4 VX")
    print(main4VX())
    print("TABLA 5 VX")
    print(main5VX())
    print("TABLA 6 VX")
    print(main6VX())
    

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


// SOLO T y X

def main1TX():
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

def main2TX():
	tabla2t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	tabla2x = [0.707 , 0.410 , 0.060 , -0.298 , -0.618, -0.856]
	n = len(tabla2x)
	Suma_x = suma_x(tabla2x)
	Suma_x2 = suma_x2(tabla2x)
	Suma_y = suma_y(tabla2t)
	Suma_xy = suma_xy(tabla2x, tabla2t)
	Delta = delta(n, Suma_x, Suma_x2)
	CofB = (int)(CoefB(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))
	return CofB

def main3TX():
	tabla3t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	tabla3x = [0.0 , 0.710 , 1.327 , 1.772 , 1.986 , 1.941]
	n = len(tabla3x)
	Suma_x = suma_x(tabla3x)
	Suma_x2 = suma_x2(tabla3x)
	Suma_y = suma_y(tabla3t)
	Suma_xy = suma_xy(tabla3x, tabla3t)
	Delta = delta(n, Suma_x, Suma_x2)
	CofB = (int)(CoefB(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))
	return CofB


def main4TX():
	tabla4x = [0.0 , 0.860 , 1.552, 1.944 , 1.958, 1.591]
	tabla4t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	n = len(tabla4x)
	Suma_x = suma_x(tabla4x)
	Suma_x2 = suma_x2(tabla4x)
	Suma_y = suma_y(tabla4t)
	Suma_xy = suma_xy(tabla4x, tabla4t)
	Delta = delta(n, Suma_x, Suma_x2)
	CofB = (int)(CoefB(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))
	return CofB

def main5TX():
	tabla5x = [2.000 , 1.806 , 1.261 , 0.471 , -0.410 , -1.211]
	tabla5t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	n = len(tabla5x)
	Suma_x = suma_x(tabla5x)
	Suma_x2 = suma_x2(tabla5x)
	Suma_y = suma_y(tabla5t)
	Suma_xy = suma_xy(tabla5x, tabla5t)
	Delta = delta(n, Suma_x, Suma_x2)
	CofB = (int)(CoefB(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))
	return CofB

def main6TX():
	tabla6x = [-1.000 , -0.809 , -0.309 , 0.309 , 0.809 , 1.000]
	tabla6t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	n = len(tabla6x)
	Suma_x = suma_x(tabla6x)
	Suma_x2 = suma_x2(tabla6x)
	Suma_y = suma_y(tabla6t)
	Suma_xy = suma_xy(tabla6x, tabla6t)
	Delta = delta(n, Suma_x, Suma_x2)
	CofB = (int)(CoefB(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))
	return CofB



// SOLO V y X
def main1VX():
	tabla1x = [1.000 , 0.951 , 0.809 , 0.588 , 0.309 , 0.000]
	tabla1v = [0.000 , -0.485 , -0.923 , -1.271 , -1.491 , -1.571]
	n = len(tabla1x)
	Suma_x = suma_x(tabla1x)
	Suma_x2 = suma_x2(tabla1x)
	Suma_y = suma_y(tabla1v)
	Suma_xy = suma_xy(tabla1x, tabla1v)
	Delta = delta(n, Suma_x, Suma_x2)
	CofB = (int)(CoefB(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))
	return CofB

def main2VX():
	tabla2x = [0.707 , 0.410 , 0.060 , -0.298 , -0.618, -0.856]
	tabla2v = [-1.283 , -1.654 , -1.811 , -1.731 , -1.427 , -0.936]
	n = len(tabla2x)
	Suma_x = suma_x(tabla2x)
	Suma_x2 = suma_x2(tabla2x)
	Suma_y = suma_y(tabla2v)
	Suma_xy = suma_xy(tabla2x, tabla2v)
	Delta = delta(n, Suma_x, Suma_x2)
	CofB = (int)(CoefB(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))
	return CofB

def main3VX():
	tabla3x = [0.0 , 0.710 , 1.327 , 1.772 , 1.986 , 1.941]
	tabla3v = [3.628 , 3.392, 2.714, 1.683 , 0.483 , -0.873]
	n = len(tabla3x)
	Suma_x = suma_x(tabla3x)
	Suma_x2 = suma_x2(tabla3x)
	Suma_y = suma_y(tabla3v)
	Suma_xy = suma_xy(tabla3x, tabla3v)
	Delta = delta(n, Suma_x, Suma_x2)
	CofB = (int)(CoefB(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))
	return CofB

def main4VX():
	tabla4x = [0.0 , 0.860 , 1.552, 1.944 , 1.958, 1.591]
	tabla4v = [4.443, 4.012, 2.801, 1.047, -0.910, -2.691]
	n = len(tabla4x)
	Suma_x = suma_x(tabla4x)
	Suma_x2 = suma_x2(tabla4x)
	Suma_y = suma_y(tabla4v)
	Suma_xy = suma_xy(tabla4x, tabla4v)
	Delta = delta(n, Suma_x, Suma_x2)
	CofB = (int)(CoefB(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))
	return CofB

def main5VX():
	tabla5x = [2.000 , 1.806 , 1.261 , 0.471 , -0.410 , -1.211]
	tabla5v = [0.0 , -1.910 , -3.448 , -4.318 , -4.349 , -3.535]
	n = len(tabla5x)
	Suma_x = suma_x(tabla5x)
	Suma_x2 = suma_x2(tabla5x)
	Suma_y = suma_y(tabla5v)
	Suma_xy = suma_xy(tabla5x, tabla5v)
	Delta = delta(n, Suma_x, Suma_x2)
	CofB = (int)(CoefB(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))
	return CofB



def main6VX():
	tabla6x = [-1.000 , -0.809 , -0.309 , 0.309 , 0.809 , 1.000]
	tabla6v = [0.000 , 1.847 , 2.988 , 2.988 , 1.847 , 0.000]
	n = len(tabla6x)
	Suma_x = suma_x(tabla6x)
	Suma_x2 = suma_x2(tabla6x)
	Suma_y = suma_y(tabla6v)
	Suma_xy = suma_xy(tabla6x, tabla6v)
	Delta = delta(n, Suma_x, Suma_x2)
	CofB = (int)(CoefB(n, Suma_x, Suma_x2,  Suma_y, Suma_xy, Delta))
	return CofB


// main()
def main():
    print("TABLA 1 TX")
    print(main1TX())
    print("TABLA 2 TX")
    print(main2TX())
    print("TABLA 3 TX")
    print(main3TX())
    print("TABLA 4 TX")
    print(main4TX())
    print("TABLA 5 TX")
    print(main5TX())
    print("TABLA 6 TX")
    print(main6TX())
    print("TABLA 1 VX")
    print(main1VX())
    print("TABLA 2 VX")
    print(main2VX())
    print("TABLA 3 VX")
    print(main3VX())
    print("TABLA 4 VX")
    print(main4VX())
    print("TABLA 5 VX")
    print(main5VX())
    print("TABLA 6 VX")
    print(main6VX())
    


if __name__ == "__main__":

    main()

### TEST CALCULO COEFICIENTE A
from CodigoProyecto import CoefiA as CA
import math

def test_CoefiA1TX():
    CoeficienteA = CA.main1TX()
    assert math.isclose(CoeficienteA, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"
    
def test_CoefiA1VX():
    CoeficienteA = CA.main1VX()
    assert math.isclose(CoeficienteA, 1), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"

def test_CoefiA2TX():
    CoeficienteA = CA.main2TX()
    assert math.isclose(CoeficienteA, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"

def test_CoefiA2VX():
    CoeficienteA = CA.main2VX()
    assert math.isclose(CoeficienteA, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"

def test_CoefiA3TX():
    CoeficienteA = CA.main3TX()
    assert math.isclose(CoeficienteA, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"

def test_CoefiA3VX():
    CoeficienteA = CA.main3VX()
    assert math.isclose(CoeficienteA, -1), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"

def test_CoefiA4TX():
    CoeficienteA = CA.main4TX()
    assert math.isclose(CoeficienteA, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"

def test_CoefiA4VX():
    CoeficienteA = CA.main4VX()
    assert math.isclose(CoeficienteA, -2), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"

def test_CoefiA5TX():
    CoeficienteA = CA.main5TX()
    assert math.isclose(CoeficienteA, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"

def test_CoefiA5VX():
    CoeficienteA = CA.main5VX()
    assert math.isclose(CoeficienteA, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"

def test_CoefiA6TX():
    CoeficienteA = CA.main6TX()
    assert math.isclose(CoeficienteA, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"

def test_CoefiA6VX():
    CoeficienteA = CA.main6VX()
    assert math.isclose(CoeficienteA, 0), f"La prueba falló. Esperado: 1.0, Obtenido: {CoeficienteA}"




### TEST CALCULO COEFICIENTE B
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


## COMO USAR CODIGO

### USO CODIGO CALCULO LINEALIZACION
Lo que realiza este codigo es calcular los nuevos datos linealixados de las 6 tablas proporcinadas por el Inge Grabriel, el metodo mas apropiado es la elevacion
al cuadrado, lo cual se creo dos metodos de linealizacion y se obtuvo los datos.

### USO CODIGO CALCULO COEFICIENTE A
se calculo los coeficientes A para cada tabla que se uso en el proyecto, para eso se creo metodos de programacion que calculan los coeficientes de cada tabla.

### USO CODIGO CALCULO COEFICIENTE B
se calculo los coeficientes B para cada tabla que se uso en el proyecto, para eso se creo metodos de programacion que calculan los coeficientes de cada tabla.

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
![Foto de el resultado de los test mediante la terminal](PytestCoefi.png)

## OBSERVACIONES
Para realizar el cambio de variable apropiado, luego de resolver con el metodo de movimiento armonico simple, viendo que en las tablas tenemos valores de 0 o 
negativos, se opto por usar el metodo de elevacion de datos al cuadrado, ya que es el mas apropiado para el tipo de  datos que manejamos con las tablas.
