def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

def myfunc():
  global x
  x = 300

myfunc()

print(x)

#expresiones lambda
x = lambda a : a + 10
print(x(5))

#varios parametros en una lambda 
x = lambda a, b : a * b
print(x(5, 6))

#lambdas en listas --> list(map())
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

numeros2 = [1, 2, 3, 4, 5]
restas = list(map(lambda x: x - 2, numeros2))
print(restas)

#ordenar listas --> sorted()
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)