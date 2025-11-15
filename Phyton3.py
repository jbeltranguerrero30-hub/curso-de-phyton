#Crea una lista con 5 productos de supermercado y muéstrala en pantalla.
SUPER_M = ["Arroz","Leche","Huevos","Pasta","Azucar"]
print("la lista del supermercado es:",SUPER_M)
#Tienes una lista con 4 comidas favoritas, cambia la segunda por un nuevo platillo.
COMIDA = ["Lasaña","Pizza","Salchipapa","Pasta"]
print("mis 4 comidas favoritas son:",COMIDA)
COMIDA[3]="Dorilocos"
print("mis 4 comidas favoritas son:",COMIDA)
#Crea una lista con 3 invitados a una fiesta, agrega dos más, y luego elimina uno.
FIESTA = ["Fabian","Tiago","Juan"]
print("la lista de invitados es:",FIESTA)
FIESTA.append("Carlos")
FIESTA.append("Orley")
print("la lista con nuevos invitados es:",FIESTA)
FIESTA.remove("Fabian")
FIESTA.remove("Tiago")
print("la lista actualizada es:",FIESTA)
#Crea una lista con 5 colores y muestra la lista en orden inverso usando reverse() o [::-1].
COLORES = ["AZUL","VERDE","ROJO","AMARILLO","MORADO"]
print("la lista de colores es:",COLORES)
print("la lista de colores al reverso es:",COLORES[::-1])
#Crea una lista con animales y usa len() para mostrar cuántos hay.
ANIMALES = ["Perro","Gato","Elefanto","Serpiente"]
print("la lista de animales es:",ANIMALES)
print("la cantidad de animales:",len(ANIMALES))
#Crea una lista con elementos repetidos y usa set() para mostrar la lista sin duplicados.
ROPA = ["Pantalon","Chaqueta","Medias","Camiseta","Sudadera","Pantalon","Chaqueta"]
print("la lista de ropa es:",ROPA)
print("la lista sin duplicados es:",set(ROPA))
#Crea una lista de números y genera una nueva lista con el cuadrado de cada número usando un bucle o comprensión de listas.
LISTA_NUMEROS = [2,4,6,8]
LISTA_NUMEROS2 = []
for NUMEROS in LISTA_NUMEROS:
    LISTA_NUMEROS2.append(NUMEROS**2)
print("la lista de numeroes es:",LISTA_NUMEROS)
print("el cudrado de los numeros es:",LISTA_NUMEROS2)
#Une dos listas (por ejemplo, frutas y verduras) en una sola y muéstrala.
FRUTAS = ["Manzana","Naranja","Mango"]
print("la lista de frutas es:",FRUTAS)
VERDURAS = ["Espinaca","Brocoli","Pepino"]
print("la lista de verduras es:",VERDURAS)
FRUTAS_VERDURAS = FRUTAS+VERDURAS
print("La lista combinada es:",FRUTAS_VERDURAS)
#De una lista de números, elimina todos los que sean menores a 5.
NUMEROS_2 = [3,4,5,12,15,18]
print("lista de numero:",NUMEROS_2)
NUMEROS_2_NUEVA =[]
for n in NUMEROS_2:
    if n>5:
        NUMEROS_2_NUEVA.append(n)
print("Lista de numeros mayores que 5:",NUMEROS_2_NUEVA)

#Crea una lista que represente el inventario de una tienda. Permite que el usuario agregue y quite productos mediante input().
INVENTARIO = ["Arroz","Pasta","Shampo","Jabon"]
print("El inventario es:",INVENTARIO)
INVENTARIO_1 =input("que productos desea agregar:").title()
INVENTARIO_2 =input("ingrese que producto desea quitar:").title()
INVENTARIO.remove(INVENTARIO_2)
INVENTARIO.append(INVENTARIO_1)
print(INVENTARIO)

#Crea una tupla que represente la ubicación (x, y) de un punto y muéstrala.
punto = (5,8)
print("La ubicacion del punto es:",punto)

#Crea una tupla con nombre, edad y ciudad, y muestra cada elemento con su etiqueta.
infomacion =("Sebastian",24,"Bogota")
print("Nombre:",infomacion[0],"Edad:",infomacion[1],"Ciudad:",infomacion[2])

#Crea una tupla con 3 frutas y asígnalas a tres variables diferentes.
frutas= ("manzana","pera","mango")
fruta1, fruta2, fruta3 = frutas

print("las frutas son:",fruta1,fruta2,fruta3)

#Intenta modificar una tupla y explica por qué da error.

ropa=("camiseta","pantalon","chaqueta")
print(ropa)
#ropa[1]= "medias" #las tuplas no son mutables
print("las tuplas no son mutables:",ropa)

#Crea dos tuplas y únelas en una sola.

colores_1=("blanco","negro","gris")
colores_2=("azul","amarillo","rojo") 
colores=(colores_1+colores_2)
print("tupla 1:",colores_1)
print("tupla 2:",colores_2)
print("tuplas unidas:",colores)

#Crea una tupla pequeña y repítela 3 veces usando el operador *.

utiles=("lapiz","cuaderno","borrador")
utiles_2=utiles*3
print("la tupla es:",utiles)
print("la tupla repetida es:",utiles_2)

#Crea una tupla de números y encuentra el valor mayor y menor usando max() y min().

numeros=(5,12,24,2,34)
print("la tupla es:",numeros)
print("el valor mayor en la tupla es:",max(numeros))
print("el valor menor en la tupla es:",min(numeros))


#Crea una lista y conviértela a tupla con tuple().

lista=["casa","carro","moto","finca"]
tupla=tuple(lista)
print("la lista es:",lista)
print("la lista convertida en tupla es:",tupla)

#Crea una tupla y verifica si un elemento está en ella usando in.

numer=(2,4,5,7,8,9)
print("la tupla es:",numer)
print("verificar si 5 esta en la tupla:",5 in numer)

#Crea una tupla y encuentra la posición de un elemento con .index().

vehiculos=("moto","carro","bici","patineta")
pos=vehiculos.index("bici")
print("la tupla es:",vehiculos)
print ("la posicion de bici es:",pos)
