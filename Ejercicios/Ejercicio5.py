text1 = "Hola"
text2 = "Mundo" 
textFinal = text1 + " " + text2
print(textFinal)

print("El saludo es: %s %s" % (text1, text2))

saludoFinal = "Saludo: {0} {1}" .format(text1, text2)
print(saludoFinal) 

saludoFinal2 = "Saludo: {x} {y}".format(x=text2, y=text1)
print(saludoFinal2)