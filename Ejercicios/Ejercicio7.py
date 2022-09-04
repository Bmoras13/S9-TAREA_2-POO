"""
Tupla: estructura de datos propia de python que permite almacenar
distintos valores, son inmutables (no cambian una vez inicializadas).
"""

tupla = (1, 2, 3)
print(tupla)

tupla2 = (13, "Bryan", 10.01, 16 + 7j, "Amargura", False)
print(tupla2)

tupla3 = (9, 2, (3, 2, 1))
print(tupla3)

print(tupla2[1])
# tupla2[1] = "Joel"
print(tupla2[-1]) #accede al ultimo elemento
print(tupla2[0:4])
print(tupla2[-2]) 

a, b, c = tupla
print(a)
print(b)
print(c)

tuplaFinal = tupla + tupla3
print(tuplaFinal)

print(tuplaFinal.count(2))
print(tuplaFinal.index(2))