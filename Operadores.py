#========================================================
#OPERADORES EN PYTHON
print("============OPERADORES ARITMETICOS=======")
a = 10
b = 5
print(f"la suma de a mas b:",a+b)  
print(f"la resta de a menos b:",a-b)
print(f"la multiplicacion de a por b es igual a:",a*b)
print(f"la division de a y b es igual a:",a/b)
print("========OPERADORES RELACIONALES=========")
print(" a == b", a==b) # == es para comparar relaciones identicas
print(" a != b", a!=b) # !=  significa diferente o relacion de diferencia
print("a < b", a < b) # relacion menor que
print("a > b", a>b)  # relacion mayor que
print("a <= b", a<=b)  # relacion menores o iguales
print("a >= b", a>=b) # relaciones mayores o iguales
print(" ============== OPERADORES LOGICOS =================")
x = True
y = False
#AND
print("x AND y", x and y)
print("X OR Y", x or y)
print("x o y", x is not y)
print("===============OPERADORES UNARIOS ==================")
z = 7
print("z es positivo",{+z}) # para designar valores positivos
print("z es negativo", {-z}) # para designar valores negativos
print("not (z > 0)", {not (z > 0)})
print("not(z > 0)", {not (-z > 0)})