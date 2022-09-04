text = "Bienvenidos a mi Tarea de P.O.O"

print(text)
print(text.lower())
print(text.upper())
print(text.title()) # convierte una cadena a un formato de titulo

print(text.find("mi")) #posision donde encuentra la cadena de o porcion

print(text.count("i")) # cantidad de ocurrencias de una letra o porsion de una cadena

textFinal = text.replace("O", "0")
print(textFinal)

valor = text.isnumeric() #arroja True o False si es una cadena
print (valor)

cadenaSeparada = text.split(" ")
print (cadenaSeparada)