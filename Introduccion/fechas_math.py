import datetime

#hora actual
x = datetime.datetime.now()

print(x)

#fechas separadas

print(x.year)
print(x.day)
print(x.minute)

#convertir tiempo a string

y = datetime.datetime(2026, 6, 1)

print(x.strftime("%B"))

#Libreria math

#min y max
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#abs()
x = abs(-7.25)

print(x)

#potencia
x = pow(4, 3)

print(x)

import math

#raiz cuadrada 
x = math.sqrt(64)

print(x)

#pi

x = math.pi
print(x)