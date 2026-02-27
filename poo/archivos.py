#abrir archivos con open()
f = open("demofile.txt")
print(f.read())

#si esta en otra ruta 
f = open("D:\\myfiles\welcome.txt")
print(f.read())

#cierre automatico --> with
with open("demofile.txt") as f:
  print(f.read())

#sacar lineas del archivo 
with open("demofile.txt") as f:
  print(f.readline())

#bucle
with open("demofile.txt") as f:
  for x in f:
    print(x)

#borrar archivos
import os
os.remove("demofile.txt")

#comprobar si el archivo existe
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#borrar directorio
os.rmdir("myfolder")