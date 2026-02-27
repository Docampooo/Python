mylist = ["apple", "banana", "cherry"]

#longitud

long = len(mylist)

print(long)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

#ultimo indice 
print(thislist[-1])

#rango
print(thislist[2:5])

print(thislist[:4])

print(thislist[2:])

print(thislist[-4:-1])

#comprobar si existe
if "apple" in mylist:
    print("Dentro!")


#cambiar un indice 
thislist[1] = "blackcurrant"
print(thislist)

#cambiar varios indices 
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#insertar
thislist.insert(2, "watermelon")
print(thislist)

#añadir
thislist.append("strawberry")
print(thislist)

#insertar otra lista

tropicales = ["mango", "pineapple", "papaya"]
thislist.extend(tropicales)
print(thislist)

#borrar 
thislist.remove("mango")
print(thislist)

#borrar indice
thislist.pop(1)
print(thislist)

#borrar primer elemento

del thislist[0]
del tropicales

#borrar lista
# thislist.clear()
# print(thislist)

#recorrer lista 
for x in thislist:
    print(x)

#recorrer lista en funcion de un indice
for i in range(len(thislist)):
    print(i+1 , thislist[i])

#con while
i = 0
while i < len(thislist):
    print(i + 1, thislist[i])
    i += 1

newlist = []

for x in thislist:
  if "a" in x:
    newlist.append(x)

print(newlist)

#ordenar listas
thislist.sort()
print(thislist)

numeros = [100, 50, 30, 1000, 20, 4000]
numeros.sort()
print(numeros)

numeros.sort(reverse = True)
print(numeros)

#ordenado por minusculas
thislist.sort(key = str.lower)

#juntar 2 listas
lista3 = thislist + numeros
print(lista3)

#borrar elementos dentro de un bucle, recorrer del reves

lista = [1, 2, 3, 4, 5, 6]

for i in range(len(lista) - 1, -1, -1):
    if lista[i] % 2 == 0:
        del lista[i]

print(lista)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)