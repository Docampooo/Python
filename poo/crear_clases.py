#crear clases
class MiClase:
    x = 5

#crear objetos
c1 = MiClase()

#sacar sus datos
print(c1.x)

#borrar objetos
del c1

#clase persona
class Person:

    #init es el constructor de la clase Person
    def __init__(self, name, age = 15):

        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Me llamo {self.name} y tengo {self.age} años")

    def cumpleaños(self):
        self.age += 1
        print(f"Felicidades! tu edad es: {self.age}")

    #metodo toString()
    def __str__(self):
        return f"{self.name} {self.age}"

per = Person("alberto")

per.greet()
per.cumpleaños()

#añadir propiedades al objeto --> solo actuan sobre el objeto creado en esta instancia

per.city = "Oslo"

print(per.name)
print(per.age)
print(per.city)

print(per)

#multiples metodos y accion sobre una lista 
class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()

class Rectangle:
    def __init__(self, width, height):
      self.width = width
      self.height = height
    
    def area(self):
      return self.width * self.height
    
r = Rectangle(5, 2)

print(r.area())

#polimorfismo
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  
  #sobreescritura
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  
  #sobreescritura
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()