#La cadena de caracteres se refiere a una serie de datos que ocupan un espacio
#Ejemplo A,1,?; JM= Y si se unen forman cadenas de caracteres
#::::::::::::::::::::::::::
print (" hola mundo")
print ("SEBASTIAN BELTRAN")
curso = "programacion uno"
print ("su curso es:", curso)
institucion = "SENA" # variable tipo texto
universidad = "SENA"
trimestre = 1 # variable tipo numero
# imprimir varias variables
print ("su curso es:", curso, "su intitucion es:",institucion, " su trimestre es:", trimestre)
print(len(institucion)) # el comando len sirve para contar los numeros caracteres
print(len(curso))
#:::::::::::::::::::::::::::::::
print(curso.upper()) # el comando upper sirve para poner la cadena en mayucula
print(curso.lower()) # el coamndo lower sirve paar poner la cadena en minusculas
#:::::::::::::::::::::::::::::::
print(institucion[0]) # los corchetes sirven para traer la posicion de la cadena
print(institucion[1])
print(institucion[2])
print(institucion[3])
#:::::::::::::::::::::::::::::::
print(institucion[0:4]) # los corchetes y los dos  puntos puntos traen un rango determinado
#CONCATENAR
print((institucion + " "+curso).upper())
#COMPARAR UNA CADENA
print(curso == institucion)
print ( institucion == universidad)
print ( "Analisis y desarrollo de sistemas".replace("sistemas","software"))
nombre = "JHOAN SEBASTIAN BELTRAN GUERRERO"
print ("correro intitucional:",(nombre[0]+nombre[6]+nombre[16:23]+nombre[24]).lower()+"@sena.edu.com")
nombre1= "JHOAN"
nombre2= "SEBASTIAN"
apellido1= "BELTRAN"
apellido2= "GUERRERO"
print("correro institucional:",(nombre1[0]+nombre2[0]+apellido1+apellido2[0]).lower()+"@sena.edu.com")