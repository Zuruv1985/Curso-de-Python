file=open("./text.txt")  #se debe colocar el ./

#print (file.read()) #file.read() para leerlo
"""
#Lectura linea a linea
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

file.close() #Cierra el archivo, liberando memoria
"""

for line in file:
    print(line)

file.close()


# forma mas comun de leer archivos, el programa cierra automaticamente el archivo una vez se termina de leer
with open ("./text.txt") as file:
    for line in file:
        print (line)