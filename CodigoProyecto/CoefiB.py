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