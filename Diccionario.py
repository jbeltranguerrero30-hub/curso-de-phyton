# ----------------------------------------------
# DICCIONARIOS Y SETS EN PYTHON - EXPLICACIÓN
# ----------------------------------------------

# DICCIONARIO:
# Un diccionario en Python es una colección no ordenada de elementos que se almacenan como pares clave-valor.
# Cada clave dentro del diccionario debe ser única, y se accede al valor a través de su clave.
# Los diccionarios se definen usando llaves {}, por ejemplo:
# persona = {"nombre": "Ana", "edad": 25}
# Son mutables (se pueden modificar), y muy útiles para representar objetos, registros, etc.
persona = {
    "id": 1,
    "nombre": "sebastian",    # clave"nombre" con valor 
    "edad": 24,               # clave "edad" con valor 24
    "profesion": "aprendiz"   # clave "profesion" con valor
}

#imprimimos el diccionario completo
print("diccionario completo",persona)

# accedemos al valor de una clave especifica
print("nombre de la persona:",persona["nombre"]) #mostrar edad

# # modificamos un valor existente
persona["edad"]=25
print ("edad actualizada", persona["edad"])    #mostrara 25


# # agregamos una nueva clave-valor al diccionario
persona ["cuidad"] = "bogota"
print("diccionario con nueva clave",persona)

# recorremos el diccionario con un bucle for
for clave, valor in persona.items():
    print(f"clave: {clave} -> valor: {valor}")
    