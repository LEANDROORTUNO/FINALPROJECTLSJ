import math

def dis(listaX, listaY, A, B):
    discrepancias_sumadas = 0
    n = len(listaX)
    
    for i in range(n):
        y_observado = listaY[i]
        x_valor = listaX[i]
        
        y_predicho = A + B * x_valor
        discrepancia = y_observado - y_predicho
        discrepancia_cuadrado = math.pow(discrepancia, 2)
        discrepancias_sumadas += discrepancia_cuadrado
        
    return discrepancias_sumadas

def varianza_residual(dis, n):
    return dis / (n - 2)

def sigmaA(sigma2, Sumx2, Delta): 
    return math.sqrt((sigma2 * Sumx2) / Delta)

def sigmaB(sigma2, n, Delta): 
    return math.sqrt((sigma2 * n) / Delta)

def main_calculos_discrepancias_errores():
        tabla1x = [1.000, 0.951, 0.809, 0.588, 0.309, 0.000] 
        tabla1t = [0.000, 0.200, 0.400, 0.600, 0.800, 1.000] 
        n = len(tabla1x)
    
        Sumx2_calc = 2.872323
        Delta_calc = 1.487841
        A_calc = 1.026756
        B_calc = -1.986326

        Suma_Discrepancias_Cuadrado = dis(tabla1x, tabla1t, A_calc, B_calc)
        sigma2_calc = varianza_residual(Suma_Discrepancias_Cuadrado, n)
        error_A = sigmaA(sigma2_calc, Sumx2_calc, Delta_calc)
        error_B = sigmaB(sigma2_calc, n, Delta_calc)
    
def main_errorA() :
        tabla1x = [1.000, 0.951, 0.809, 0.588, 0.309, 0.000] 
        tabla1t = [0.000, 0.200, 0.400, 0.600, 0.800, 1.000] 
        n = len(tabla1x)
    
        Sumx2_calc = 2.872323
        Delta_calc = 1.487841
        A_calc = 1.026756
        B_calc = -1.986326

        Suma_Discrepancias_Cuadrado = dis(tabla1x, tabla1t, A_calc, B_calc)
        sigma2_calc = varianza_residual(Suma_Discrepancias_Cuadrado, n)
        error_A = sigmaA(sigma2_calc, Sumx2_calc, Delta_calc)
        return error_A
def main_errorB () :
        tabla1x = [1.000, 0.951, 0.809, 0.588, 0.309, 0.000] 
        tabla1t = [0.000, 0.200, 0.400, 0.600, 0.800, 1.000] 
        n = len(tabla1x)
    
        Sumx2_calc = 2.872323
        Delta_calc = 1.487841
        A_calc = 1.026756
        B_calc = -1.986326

        Suma_Discrepancias_Cuadrado = dis(tabla1x, tabla1t, A_calc, B_calc)
        sigma2_calc = varianza_residual(Suma_Discrepancias_Cuadrado, n)
        error_B = sigmaB(sigma2_calc, n, Delta_calc)
        return error_B