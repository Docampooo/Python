import sys

#print(sys.version)

#Comentarios en python!!!

print("Hola con cambio de linea")
print("Hola sin cambio de linea", end= " ")
print("misma linea")

print(500)

print(5 + 2)

print("combinado!", 20, "con espacios")

#Variables

nombre = "Nico"
edad = 20

print(nombre, edad)

#casting

edad = str(20)
edad = float(20)

#tipos

print(type(edad))

#varias variables asignadas al mismo tiempo

x, y, z = 90, 120, 180

print(x, y, z)

#de array a variables

frutas = ["manzana", "platano", "melocoton"]

m, p, z = frutas

print(m, p, z)

#Las variables fuera de funciones se pueden utilizar por cualquier funcion

def prueba():
    print(m)

prueba()

#crear variable global dentro de una funcion

def prueba2():
    global fun
    fun = "Funcion!"

prueba2()
print("El resultado es:", fun)


#Cambiar valor de una variable global dentro de una funcion

def prueba3():
    global m
    m = "No manzana"

print(m)

prueba3()

print(m)

#operadores 

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

x = 5

print(1 < x < 10)

print(1 < x and x < 10)

print(" - - - ")

#operador is 

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

print(" - - - ")
#Diferencia con == 

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

print(" - - - ")
# in 

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)