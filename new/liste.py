liste = [
    {"name": "john", "telephone": 666666601, "age": 23},
    {"name": "jose", "telephone": 777777777, "age": 33},
    {"name": "laura", "telephone": 888888888, "age": 43},
]
# Append new directory
liste.append({"name": "pop", "telephone": 1010101, "age": 55})

# Print updated list
print(liste)
print(type(liste))

# Print the names
for i in range(len(liste)):
    print(liste[i].get('name'))
    
    
for x in liste:
    print(f"{x['name']} | {x['telephone']} | {x['age']}")

