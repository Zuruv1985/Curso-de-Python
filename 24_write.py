with open ("./text.txt", "w+") as file: #se agrega el r+ para tener permisos de escritura y de lectura
    #con w+ se modifica todo el contenido del archivo por las nuevas lineas
    for line in file:
        print (line)

    file.write("\nSe agregan nuevas lineas de escritura en el archivo text.txt")
    file.write("\nSe agregan nuevas lineas de escritura en el archivo text.txt")
