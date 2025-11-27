
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


# SOLO T y X

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



# SOLO V y X
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

def promedio():
    Lista = [main1TX(), main2TX(), main3TX(), main4TX(), main5TX(), main6TX(), main1VX(), main2VX(), main3VX(), main4VX(), main5VX(), main6VX()]
    n = len(Lista)
    suma = 0
    promedio = 0
    for i in range(0, n - 1, 1):
        suma = suma + Lista[i]
    promedio = suma / n
    return promedio


# main()
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
    
