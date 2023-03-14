"""CRUD
C=Create
R=Read
U=
D=Delete



funcion.
    add(): Añade un elemento.

    update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.

    discard(): Elimina un elemento y si ya existe no lanza ningún error.

    remove(): Elimina un elemento y si este no existe lanza el error “keyError”.

    pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.

    clear(): Elimina todo el contenido del conjunto.

"""

set_countries={"col","mex","bol"}
print (set_countries)

Size=len(set_countries)
print (Size)

print("col" in set_countries) #True
print("pe" in set_countries)  #False

#add

set_countries.add("pe") #agregar un elemnento a un conjunto
print (set_countries)
set_countries.add("pe") #se intenta agregar de nuevo a "pe" 
print (set_countries) #No se imprime en pantalla dos veces el elemento "pe"
 #update
set_countries.update({"ar","ec","pe"})  #añadir mas de un elemento al conjunto
print (set_countries)

#remove

set_countries.remove("col")
print (set_countries)

#set_countries.remove("arg")
#print(set_countries)   #tira un error y el programa se detiene, pues arg no está en el conjunto

set_countries.discard("arg")
print(set_countries) #de esta forma el programa no se detiene

set_countries.add("arg")
print(set_countries)

set_countries.discard("ar")
print (set_countries)

set_countries.clear()
print (set_countries) #elimina todos los elementos del conjunto



