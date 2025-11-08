#::::::::::: 1 :::::
x = int(input("numero 1:"))
y = int(input("numero 2:"))
print("la suma es:",y+x)
#::::::::::: 3 ::::::
base = float (input("base:"))
altura = float (input("altura:"))
print("El area del tringulo es:", (base*altura)/2)
#:::::::::::: 5 ::::::
a = int(input("numero 1:"))
b = int(input("numero 2:"))
potencia = a**b
print("la potencia de a^b:",potencia)
#::::::::::: 7 ::::::::
E = int(input("Su edad:"))
F = 18
print ("Mayor de edad:", E >= F)
#:::::::::: 9 :::::::::
cadena_1 = str(input("ingresa cadena 1:"))
cadena_2 = str(input("ingresa cadena 2:"))
igual = cadena_1==cadena_2
print("Las cadenas son iguales:", igual)
#:::::::::: 11 ::::::::
nombre = input ("primer nombre")
identificacion = input ("numero de cedula")
usuario_1 = (nombre.lower()+identificacion[-3:] )
contraseña_1 = (identificacion)
usuario = input("usuario: su primer nombre minusculas y sus ultimos 3 digitos de la cedula:")
contraseña = input(" contraseña : su numero de identificacion")
U = usuario_1 == usuario
V = contraseña_1 == contraseña
print("usuario y contraseña:", U and V)

