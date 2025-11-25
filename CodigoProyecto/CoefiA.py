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

# SOLO T y X
def main1TX():
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

def main2TX():
    #listas de prueba:
	tabla2x = [0.707 , 0.410 , 0.060 , -0.298 , -0.618, -0.856]
	tabla2t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	#Todas las listas proporcionadas por el Ing.Gabriel son de tamaño 6
	n = len(tabla2x)
	Sumx = sumx(tabla2x)
	Sumx2 = sumx2(tabla2x)
	Sumy = sumy(tabla2t)
	Sumxy = sumxy(tabla2x, tabla2t)
	Delta = delta(n, Sumx, Sumx2)
	CofA = (int)(CoeficienteA(Sumx, Sumx2,  Sumy, Sumxy, Delta))
	return CofA
	

def main3TX():
    #listas de prueba:
	tabla3x = [0.0 , 0.710 , 1.327 , 1.772 , 1.986 , 1.941]
	tabla3t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	#Todas las listas proporcionadas por el Ing.Gabriel son de tamaño 6
	n = len(tabla3x)
	Sumx = sumx(tabla3x)
	Sumx2 = sumx2(tabla3x)
	Sumy = sumy(tabla3t)
	Sumxy = sumxy(tabla3x, tabla3t)
	Delta = delta(n, Sumx, Sumx2)
	CofA = (int)(CoeficienteA(Sumx, Sumx2,  Sumy, Sumxy, Delta))
	return CofA

def main4TX():
    #listas de prueba:
	tabla4x = [0.0 , 0.860 , 1.552, 1.944 , 1.958, 1.591]
	tabla4t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	#Todas las listas proporcionadas por el Ing.Gabriel son de tamaño 6
	n = len(tabla4x)
	Sumx = sumx(tabla4x)
	Sumx2 = sumx2(tabla4x)
	Sumy = sumy(tabla4t)
	Sumxy = sumxy(tabla4x, tabla4t)
	Delta = delta(n, Sumx, Sumx2)
	CofA = (int)(CoeficienteA(Sumx, Sumx2,  Sumy, Sumxy, Delta))
	return CofA

def main5TX():
    #listas de prueba:
	tabla5x = [2.000 , 1.806 , 1.261 , 0.471 , -0.410 , -1.211]
	tabla5t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	#Todas las listas proporcionadas por el Ing.Gabriel son de tamaño 6
	n = len(tabla5x)
	Sumx = sumx(tabla5x)
	Sumx2 = sumx2(tabla5x)
	Sumy = sumy(tabla5t)
	Sumxy = sumxy(tabla5x, tabla5t)
	Delta = delta(n, Sumx, Sumx2)
	CofA = (int)(CoeficienteA(Sumx, Sumx2,  Sumy, Sumxy, Delta))
	return CofA

def main6TX():
    #listas de prueba:
	tabla6x = [-1.000 , -0.809 , -0.309 , 0.309 , 0.809 , 1.000]
	tabla6t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	#Todas las listas proporcionadas por el Ing.Gabriel son de tamaño 6
	n = len(tabla6x)
	Sumx = sumx(tabla6x)
	Sumx2 = sumx2(tabla6x)
	Sumy = sumy(tabla6t)
	Sumxy = sumxy(tabla6x, tabla6t)
	Delta = delta(n, Sumx, Sumx2)
	CofA = (int)(CoeficienteA(Sumx, Sumx2,  Sumy, Sumxy, Delta))
	return CofA

# SOLO V Y X

def main1VX():
    #listas de prueba:
	tabla1x = [1.000 , 0.951 , 0.809 , 0.588 , 0.309 , 0.000]
	tabla1v = [0.000 , -0.485 , -0.923 , -1.271 , -1.491 , -1.571]
	#Todas las listas proporcionadas por el Ing.Gabriel son de tamaño 6
	n = len(tabla1x)
	Sumx = sumx(tabla1x)
	Sumx2 = sumx2(tabla1x)
	Sumy = sumy(tabla1v)
	Sumxy = sumxy(tabla1x, tabla1v)
	Delta = delta(n, Sumx, Sumx2)
	CofA = (int)(CoeficienteA(Sumx, Sumx2,  Sumy, Sumxy, Delta))
	return CofA


def main2VX():
    #listas de prueba:
	tabla2x = [0.707 , 0.410 , 0.060 , -0.298 , -0.618, -0.856]
	tabla2v = [-1.283 , -1.654 , -1.811 , -1.731 , -1.427 , -0.936]
	#Todas las listas proporcionadas por el Ing.Gabriel son de tamaño 6
	n = len(tabla2x)
	Sumx = sumx(tabla2x)
	Sumx2 = sumx2(tabla2x)
	Sumy = sumy(tabla2v)
	Sumxy = sumxy(tabla2x, tabla2v)
	Delta = delta(n, Sumx, Sumx2)
	CofA = (int)(CoeficienteA(Sumx, Sumx2,  Sumy, Sumxy, Delta))
	return CofA

def main3VX():
    #listas de prueba:
	tabla3x = [0.0 , 0.710 , 1.327 , 1.772 , 1.986 , 1.941]
	tabla3v = [3.628 , 3.392, 2.714, 1.683 , 0.483 , -0.873]
	#Todas las listas proporcionadas por el Ing.Gabriel son de tamaño 6
	n = len(tabla3x)
	Sumx = sumx(tabla3x)
	Sumx2 = sumx2(tabla3x)
	Sumy = sumy(tabla3v)
	Sumxy = sumxy(tabla3x, tabla3v)
	Delta = delta(n, Sumx, Sumx2)
	CofA = (int)(CoeficienteA(Sumx, Sumx2,  Sumy, Sumxy, Delta))
	return CofA

def main4VX():
    #listas de prueba:
	tabla4x = [0.0 , 0.860 , 1.552, 1.944 , 1.958, 1.591]
	tabla4v = [4.443, 4.012, 2.801, 1.047, -0.910, -2.691]
	#Todas las listas proporcionadas por el Ing.Gabriel son de tamaño 6
	n = len(tabla4x)
	Sumx = sumx(tabla4x)
	Sumx2 = sumx2(tabla4x)
	Sumy = sumy(tabla4v)
	Sumxy = sumxy(tabla4x, tabla4v)
	Delta = delta(n, Sumx, Sumx2)
	CofA = (int)(CoeficienteA(Sumx, Sumx2,  Sumy, Sumxy, Delta))
	return CofA

def main5VX():
    #listas de prueba:
	tabla5x = [2.000 , 1.806 , 1.261 , 0.471 , -0.410 , -1.211]
	tabla5v = [0.0 , -1.910 , -3.448 , -4.318 , -4.349 , -3.535]
	#Todas las listas proporcionadas por el Ing.Gabriel son de tamaño 6
	n = len(tabla5x)
	Sumx = sumx(tabla5x)
	Sumx2 = sumx2(tabla5x)
	Sumy = sumy(tabla5v)
	Sumxy = sumxy(tabla5x, tabla5v)
	Delta = delta(n, Sumx, Sumx2)
	CofA = (int)(CoeficienteA(Sumx, Sumx2,  Sumy, Sumxy, Delta))
	return CofA

def main6VX():
    #listas de prueba:
	tabla6x = [-1.000 , -0.809 , -0.309 , 0.309 , 0.809 , 1.000]
	tabla6v = [0.000 , 1.847 , 2.988 , 2.988 , 1.847 , 0.000]
	#Todas las listas proporcionadas por el Ing.Gabriel son de tamaño 6
	n = len(tabla6x)
	Sumx = sumx(tabla6x)
	Sumx2 = sumx2(tabla6x)
	Sumy = sumy(tabla6v)
	Sumxy = sumxy(tabla6x, tabla6v)
	Delta = delta(n, Sumx, Sumx2)
	CofA = (int)(CoeficienteA(Sumx, Sumx2,  Sumy, Sumxy, Delta))
	return CofA

# MAIN
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