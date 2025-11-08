#======================================

# 1. Contar cuántos caracteres tiene la frase (incluyendo espacios)
frase = "Hola mundo"
print(len(frase))
# 2. Convertir el nombre a mayúsculas
nombre = "juan perez"
print(nombre.upper())
# 3. Contar cuántas veces aparece la letra "a" en el texto
texto = "La casa está vacía"

contador = texto.count("a")
contador2 = texto.count("á")
print(contador+contador2)

# 4. Mostrar la palabra repetida 5 veces, separada por espacios
palabra = "Python"
print((palabra+" ")*5)
# 5. Mostrar la última letra de la cadena
mensaje = "Programación"
print(mensaje[-1:])
# 6. Mostrar la cadena al revés
cadena = "Hola Mundo"
print(cadena[::-1])
# 7. Reemplazar "Java" por "Python" en la frase
frase = "Me gusta Java"
frase2 = frase.replace ("Java", "Python") 
print(frase2)
# 8. Mostrar solo los primeros 4 caracteres del título
titulo = "Introducción"
print (titulo[:4])
# 9. Contar cuántas palabras tiene la oración (separadas por espacios)
oracion = "Python es divertido"
palabras= oracion.split()
cuantas = len(palabras)
print (cuantas)
# 10. Convertir la cadena a formato título → "El Señor De Los Anillos"
libro = "el señor de los anillos"
print(libro.title())
# 11. Quitar los espacios en blanco al inicio y al final del saludo
saludo = "   Hola mundo   "
print (saludo.strip())
# 12. Verificar si la cadena contiene solo letras (sin números ni símbolos)
codigo = "Python3"
print (codigo.isalpha())
# 13. Mostrar las iniciales del nombre completo → "C.A.G."
nombre_completo = "Carlos Alberto García"
nom1= "Carlos"
nom2= "Alberto"
apell1= "Garcia"
print(nom1[0]+"."+nom2[0]+ "."+apell1[0])
# 14. Reemplazar las vocales con "_" (guion bajo)
frase= "Estoy aprendiendo Python"
vocales = "aeiouAEIOU"
for v in vocales:
    frase = frase.replace(v, "_")
print(frase)
# 15. Crear un nombre de usuario con las 2 primeras letras del nombre + 3 últimas del apellido, en minúsculas
nombre = "Luis"
apellido = "Martínez"
usuario = (nombre[:2]+apellido[-3:]).lower()
print (usuario)