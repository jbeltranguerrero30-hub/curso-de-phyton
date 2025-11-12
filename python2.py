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
#:::::::::: 13 :::::::
G = int(input("ingrese un valor:"))
F = int(input("ingrese un valor:"))
H = int(input("ingrese un valor negativo:"))
print ("G=<0 RO F=<0 OR H=<0:", G<=0 or F<=0 or H<=0)
#::::::::: 15 :::::::::
valor = int(input("ingrese un valor entre 30 y 50  que sea par"))
print("el valor esta entre 30-50 y es par:", valor>30 and valor<50 and valor % 2 == 0)
#::::::::: 17 :::::::::
PRECIO = float(input("ingresa el precio"))
PRECIO *= 0.8
print("El precio con el descuento del 20%:", PRECIO )
#:::::::::: 19 ::::::::
