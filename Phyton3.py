#Crea una lista con 5 productos de supermercado y muéstrala en pantalla.
SUPER_M = ["Arroz","Leche","Huevos","Pasta","Azucar"]
print(SUPER_M)
#Tienes una lista con 4 comidas favoritas, cambia la segunda por un nuevo platillo.
COMIDA = ["Lasaña","Pizza","Salchipapa","Pasta"]
COMIDA[3]="Dorilocos"
print(COMIDA)
#Crea una lista con 3 invitados a una fiesta, agrega dos más, y luego elimina uno.
FIESTA = ["Fabian","Tiago","Juan"]
print(FIESTA)
FIESTA.append("Carlos")
FIESTA.append("Orley")
print(FIESTA)
FIESTA.remove("Fabian")
FIESTA.remove("Tiago")
print(FIESTA)
#Crea una lista con 5 colores y muestra la lista en orden inverso usando reverse() o [::-1].
COLORES = ["AZUL","VERDE","ROJO","AMARILLO","MORADO"]
print(COLORES)
print(COLORES[::-1])
#Crea una lista con animales y usa len() para mostrar cuántos hay.
ANIMALES = ["Perro","Gato","Elefanto","Serpiente"]
print(len(ANIMALES))