#LISTAS EN PYTHON
#Las listas son datos que tienen como caracteristicas que son mutables
#la listas son ordenadas
#Ejemplo
estudiante = ["ERIK","ZULETA","ANGIE","KAROL","LEONARDO"]
print (estudiante) # Imprimir la lista
print (len(estudiante)) #Imprimir la cantidad de datos de la lista
print (estudiante[2])  #Imprimir la posicion de la lista
estudiante[2] = "LORENA" #Modificar o mutar la lista
print (estudiante) #Imprimir la lista nuevamente
estudiante.append("DIEGO") #append sirve para agregar un objeto a la lista
print(estudiante) #Imprimir lista 
estudiante.remove("ERIK") #Remove sirve para eliminar un objeto de la lista
print(estudiante)
del estudiante[3] #del sirve para eliminar una posicion
print(estudiante)
print("mostrar todas las frutas")
for estudiante in estudiante:
    print(" ",estudiante)
#=============================
#=============TUPLAS==========
#=============================
# LAS TUPPLAS SON ORDENADAS
# LAS TUPLAS NO SON MUTABLES
# LAS TUPLAS SE DEFINEN CON ()   
equipos = ("nacional","millonarios","santafe","junior","america","tolima")
print(equipos)
print("el equipo es",equipos[3]) #Muestra la posicion
#=========
