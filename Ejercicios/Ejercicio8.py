"""
Listas: estructura de datos que permiten almacenar valores (es el equivalente
a los arrays en otros leenguajes de programacion).

son des estructuras dinamicas, son mutables.
"""

lista1 = ["Bryan", 25, 98.3, True, "Joel", 13.10]
print(lista1)
print ( lista1[ : ])
print ( lista1[2])
print ( lista1[-1])

print ( lista1[0:3])
print ( lista1[:2])
print ( lista1[3:])

lista1.append("UNEMI")
print(lista1)

lista1.insert(4, "Ecuador")
print(lista1)

lista1.extend(["Alejandro", 110, False])
print(lista1)

print(lista1.index("Ecuador"))

lista1.remove(98.3)
print(lista1)

lista1.pop()
print(lista1)

lista2 = ["Chiclayo", "Izma"]
lista3 = lista1 + lista2
print (lista3) 

print (lista2 * 4)

print ("Joel" in lista1)