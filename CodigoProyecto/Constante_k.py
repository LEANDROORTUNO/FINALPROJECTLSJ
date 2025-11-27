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

def main2():
    print(promedio_k_tabla1())
    print(promedio_k_tabla2())
    print(promedio_k_tabla3())
    print(promedio_k_tabla4())
    print(promedio_k_tabla5())
    print(promedio_k_tabla6())
