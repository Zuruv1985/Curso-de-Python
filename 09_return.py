def find_volume (lenght=1, widht=1, depth=1): #Se pueden agregar valores por defecto o variables en el proceso
    return lenght*widht*depth, lenght, "Hola" #Se pueden retornar varios returns a la vez

result, widht, text = find_volume(widht=10) #se puede enviar uno o varios parametros de entrada

print (result)   #puede retornar diferentes valores, si se colocan antes del igual en el paso anterior
print (widht)
print (text)