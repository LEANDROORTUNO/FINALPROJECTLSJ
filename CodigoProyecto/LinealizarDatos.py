import math
#Parte de la tarea para el informe:
#poetry run python -m CodigoProyecto.GenerarGrafico Csv/tabla1.csv

#En Tabla XyT
def TablaXyT(tabla, tabla2):
    tablauxXyT = []
    aux = 0
    for t in range(0,len(tabla2),1):
        aux = math.pow(tabla2[t], 2)
        tablauxXyT.append(aux)
    return tablauxXyT 
    
#En Tabla XyV
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



#no olvidar guardar los datos en un archivo cvs


# METODOS MAIN: 
# main Tabla 1
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

# main Tabla 2
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


# main Tabla 3
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


# main Tabla 4
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


# main Tabla 5
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


# main Tabla 6
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
	
#MAIN: para todas las funciones:
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
        
    