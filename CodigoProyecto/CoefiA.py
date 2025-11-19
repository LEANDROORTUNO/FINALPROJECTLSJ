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