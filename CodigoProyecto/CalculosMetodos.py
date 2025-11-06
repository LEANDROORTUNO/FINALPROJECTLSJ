import math
#Parte de la tarea para el informe:

#poetry run python -m labfisica.CsvScatterPlot tests/data/data.csv

#PARTE Tabla 1
# metodos para calcular la propagacion de errores(cambio de variable)
def Tabla1Cam(tabla1t, tabla1v, tabla1x):
	listaCamx = []
	listaCamy = []
	listaCamz = []
	camx = 0
	camy = 0
	camz = 0
	print("Tabla1 con cambio de variable: \n")
	print("columna x: \n")
	for x in range (0, len(tabla1t), 1):
		camx = math.pow(tabla1t[x],2)
		listaCamx.append(camx)
		print(listaCamx[x])
	print("columna y:\n")
	for y in range (0, len(tabla1v), 1):
		camy = math.pow(tabla1v[y],  2)
		listaCamy.append(camy)
		print(listaCamy[y])
	print("columna z:\n")
	for z in range (0, len(tabla1x), 1):
		camz = math.pow(tabla1x[z],  2)
		listaCamz.append(camz)
		print(listaCamz[z])


#PARTE Tabla 2
# metodos para calcular la propagacion de errores(cambio de variable)
def Tabla2Cam(tabla2t, tabla2v, tabla2x):
	listaCamx = []
	listaCamy = []
	listaCamz = []
	camx = 0
	camy = 0
	camz = 0
	print("Tabla2 con cambio de variable : \n")
	print("columna x : \n")
	for x in range(0, len(tabla2t), 1):
		camx = math.pow(tabla2t[x], 2)
		listaCamx.append(camx)
		print(listaCamx[x])
	print("columna y : \n")
	for y in range(0, len(tabla2v), 1):
		camy = math.pow(tabla2v[y], 2)
		listaCamy.append(camy)
		print(listaCamy[y])
	print("columna z : \n")
	for z in range(0, len(tabla2x), 1):
		camz = math.pow(tabla2x[z], 2)
		listaCamz.append(camz)
		print(listaCamz[z])
	

#PARTE Tabla 3
# metodos para calcular la propagacion de errores(cambio de variable)
def Tabla3Cam(tabla3t, tabla3v, tabla3x):
	listaCamx = []
	listaCamy = []
	listaCamz = []
	camx = 0
	camy = 0
	camz = 0
	print("Tabla 3 con cambio de variable : \n")
	print("columna x : \n")
	for x in range(0, len(tabla3t), 1):
		camx = math.pow(tabla3t[x], 2)
		listaCamx.append(camx)
		print(listaCamx[x])
	print("columna y : \n")
	for y in range(0, len(tabla3v), 1):
		camy = math.pow(tabla3v[y], 2)
		listaCamy.append(camy)
		print(listaCamy[y])
	print("columna z : \n")
	for z in range(0, len(tabla3x), 1):
		camz = math.pow(tabla3x[z], 2)
		listaCamz.append(camz)
		print(listaCamz[z])


#PARTE Tabla 4
# metodos para calcular la propagacion de errores(cambio de variable)
def Tabla4Cam(tabla4t, tabla4v, tabla4x):
	listaCamx = []
	listaCamy = []
	listaCamz = []
	camx = 0
	camy = 0
	camz = 0
	print("Tabla 4 con cambio de variable: \n")
	print("columna x: \n")
	for x in range (0, len(tabla4t), 1):
		camx = math.pow(tabla4t[x],2)
		listaCamx.append(camx)
		print(listaCamx[x])
	print("columna y:\n")
	for y in range (0, len(tabla4v), 1):
		camy = math.pow(tabla4v[y],  2)
		listaCamy.append(camy)
		print(listaCamy[y])
	print("columna z:\n")
	for z in range (0, len(tabla4x), 1):
		camz = math.pow(tabla4x[z],  2)
		listaCamz.append(camz)
		print(listaCamz[z])


#PARTE Tabla 5
# metodos para calcular la propagacion de errores(cambio de variable)
def Tabla5Cam(tabla5t, tabla5v, tabla5x):
	listaCamx = []
	listaCamy = []
	listaCamz = []
	camx = 0
	camy = 0
	camz = 0
	print("Tabla 5 con cambio de variable : \n")
	print("columna x : \n")
	for x in range(0, len(tabla5t), 1):
		camx = math.pow(tabla5t[x], 2)
		listaCamx.append(camx)
		print(listaCamx[x])
	print("columna y : \n")
	for y in range(0, len(tabla5v), 1):
		camy = math.pow(tabla5v[y], 2)
		listaCamy.append(camy)
		print(listaCamy[y])
	print("columna z : \n")
	for z in range(0, len(tabla5x), 1):
		camz = math.pow(tabla5x[z], 2)
		listaCamz.append(camz)
		print(listaCamz[z])


#PARTE Tabla 6
# metodos para calcular la propagacion de errores(cambio de variable)
def Tabla6Cam(tabla6t, tabla6v, tabla6x):
	listaCamx = []
	listaCamy = []
	listaCamz = []
	camx = 0
	camy = 0
	camz = 0
	print("Tabla 6 con cambio de variable : \n")
	print("columna x : \n")
	for x in range(0, len(tabla6t), 1):
		camx = math.pow(tabla6t[x], 2)
		listaCamx.append(camx)
		print(listaCamx[x])
	print("columna y : \n")
	for y in range(0, len(tabla6v), 1):
		camy = math.pow(tabla6v[y], 2)
		listaCamy.append(camy)
		print(listaCamy[y])
	print("columna z : \n")
	for z in range(0, len(tabla6x), 1):
		camz = math.pow(tabla6x[z], 2)
		listaCamz.append(camz)
		print(listaCamz[z])




#no olvidar guardar los datos en un archivo cvs


# METODOS MAIN: 
# main Tabla 1
def mainTabla1():
	#lista de datos del cilindro
	tabla1t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	tabla1x = [1.000 , 0.951 , 0.809 , 0.588 , 0.309 , 0.000]
	tabla1v = [0.000 , -0.485 , -0.923 , -1.271 , -1.491 , -1.571]

	#metodo cambbio de variable:
	Tabla1Cam(tabla1t, tabla1v, tabla1x)

# main Tabla 2
def mainTabla2():
	# lista de datos de los discos
	tabla2t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	tabla2x = [0.000 , 0.710 , 1.327 , 1.772 , 1.986 , 1.941]
	tabla2v = [3.628 , 3.392 , 2.714 , 1.683 , 0.433 , -0.873]
	
	#metodo cambio de variable
	Tabla2Cam(tabla2t , tabla2v, tabla2x)


# main Tabla 3
def mainTabla3():
	#lista de datos de la esfera
	tabla3t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	tabla3x = [2.000 , 1.806 , 1.261 , 0.471 , -0.410 , -1.211]
	tabla3v = [0.000 , -1.910 , -3.448 , -4.318 , -4.349 , -3.535]
	
	#metodo cambio de variable
	Tabla3Cam(tabla3t, tabla3v, tabla3x)


# main Tabla 4
def mainTabla4():
	#lista de datos del cilindro
	tabla4t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	tabla4x = [0.707 , 0.410 , 0.060 , -0.298 ,-0.618 , -0.856]
	tabla4v = [-1.283 , -1.654 , -1.811 , -1.731 , -1.427 , -0.936]

	#metodo cambbio de variable:
	Tabla4Cam(tabla4t, tabla4x, tabla4v)


# main Tabla 5
def mainTabla5():
	#lista de datos del cilindro
	tabla5t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	tabla5x = [0.000 , 0.800 , 1.552 , 1.944 , 1.958 , 1.591]
	tabla5v = [4.443 , 4.012 , 2.801 , 1.047 , -0.910 , -2.691]
	
	#metodo cambbio de variable:
	Tabla5Cam(tabla5t, tabla5x, tabla5v)


# main Tabla 6
def mainTabla6():
	#lista de datos del cilindro
	tabla6t = [0.000 , 0.200 , 0.400 , 0.600 , 0.800 , 1.000]
	tabla6x = [-1.000 , -0.809 , -0.309 , 0.309 , 0.809 , 1.000]
	tabla6v = [0.000 , 1.847 , 2.988 , 2.988 , 1.847 , 0.000]
	
	#metodo cambbio de variable:
	Tabla6Cam(tabla6t, tabla6x, tabla6v)