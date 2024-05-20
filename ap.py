

# -*- coding: utf-8 -*-
# PODEMOS VER EL SCOPE DE LAS VARIABLES Y FUNCIONES
name = "Vicents"

def saludar():
    print("Hola " +  name)

print(name)
saludar()    



name = "Vicents"

def saludar():
    name = "Sergi"
    print("Hola " +  name)

saludar()
print(name)



import datetime
actual_year = datetime.date.today().year

user1 = {"name": "Krisel", "isAdmin": True, "bith": 1989, "parent": False}
user2 = {"name": "JM", "isAdmin": True, "bith": 2014, "parent": True}

def can_access(user):
    age = actual_year - user["bith"]
    if not user["isAdmin"] or age < 18:
        return False
    return True

def access_sys(user): 
    if not can_access(user):
        print(user["name"] + " Acceso denegado") 
        return

        print(user["name"] + " Ha accedido al sistema ")
        print("Ha accedido al sistema ")
        print("Ha accedido al sistema ")
        print("Ha accedido al sistema ")
        print("Ha accedido al sistema ")

access_sys(user1)    
access_sys(user2)

# -*- coding: utf-8 -*-


# -*- Asigna tu nombre a una variable -*-
miNombre = "Andrea"

print("Mi nombre es: " + miNombre)



# -*- Imprime el número de caracteres de tu nombre -*-
miNombre = "Andrea"
nombre_caracteres = len(miNombre)

print("Mi nombre tiene  " + str(nombre_caracteres))


# -*- Imprime tu nombre en mayúsculas -*-
miNombre = "Andrea"
nombre_mayusculas = miNombre.upper()

print(nombre_mayusculas)