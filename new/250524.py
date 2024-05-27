def saludar():
    print("hola youssef")
saludar()

#def saludarpersona(persona="mundo"):
#    print(f"buenos dias, {persona}")
#   saludarpersona("sergi")

def cambio(a):
    return a * 2  # Se define una operación coherente para la función

valor = cambio(5)
print(valor)
#def cambio(a):
 #   return ayay
#valor=cambio(5)
#print(valor)

def sumar(a:int,b:int)->int:
    return a+b
print(sumar(4,5))

#def saludarpersona(persona="mundo"):
 #   print("buenos dias{persona}")
  #  saludarpersona("clouder")
#-------------
def saludarpersona(persona="mundo"):
    print(f"buenos dias {persona}")

# Call the function to test it
saludarpersona("clouder")

# Lambda function to add two numbers
multiplica = lambda a, b: a + b
print(multiplica(3, 5))  # This will print 8

# Regular function to multiply two numbers
def multiplica(a, b):
    return a * b

print(multiplica(3, 5))  # This will print 15
# otro ex :calcular el volumen de cilindro

#with open('file.txt', 'r') as archivo:
 #       content = archivo.read()
  #      print(content)

with open('new/file.txt', 'a') as archivo:
   archivo.write("Este es un contenido adicional2.\n")
#---------------------------function
numeros =(1,2,3,4,5)
def cubico(number):
    return number**3
result = map(cubico, numeros)
resultLambda =map(lambda x: x**3,numeros)

print(list(result))
#print(list(resultLambda))
#--------------------
numeros=[1,2,3,4,5,6,7,8,9]
result = filter(lambda x:x>5,numeros)
print(list(result))
#--------
from functools import reduce
numeros=[1,2,3,4,5,6,7,8,9]
result = reduce(lambda x,y: x+y, numeros)
print(result)