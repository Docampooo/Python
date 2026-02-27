#python puede imprimir comillas dentro de strings

print("Me dicen que programo 'Bien'")

#Los strings son arrays

a = "Me dicen que programo 'Bien'"

print(a[1]) # --> e

#recorrar strings con bucle

for x in a:
    print(x)

#longitud de un string

long = len(a)

print(long)

#contains en las cadenas --> booleano

respuesta = "cen" in a
print(respuesta)

if "ien" in a:
    print("Dentro!")

error = "main" not in a
print(error)

#Slicing

trozo = a[2:10]

print(trozo)

inicio = a[:10]

print(inicio)

final = a[10:]

print(final)

b = "Hello, World!"
print(b[-5:-2])

#modificar cadenas

c = a.upper().strip()
d = a.lower().strip()

print(c, d)

#remplazar fragmentos de cadenas

e = a.replace("a", "o")

print(e)

divisiones = a.split(" ")

print(divisiones)

#string format

txt = f"Cadena: {a}"

print(txt)

num = 23
precio = f"El coste es de {num:.2f} dolares"

print(precio)

precio = f"El coste ha cambiado, ahora es de {num / 2} dolares"

print(precio)

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt)

#indices nombrados 
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))