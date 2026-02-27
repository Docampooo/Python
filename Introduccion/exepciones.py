try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

#lanzar excepcion --> raise()

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

#comprobar tipos 

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")