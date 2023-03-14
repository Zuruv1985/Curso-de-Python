#set=conjuntos 
#se utilizan las llaves
#no repite elementos

set_countries={"col","mex","bol"}
print (set_countries)
print(type(set_countries))

set_numbers={1, 2, 2, 443, 23}
print(set_numbers)
print(type(set_numbers))

#se pueden combinar tipos de datos
#El orden de los elementos no importan
set_types={1, "Hola", False, 12,12}
print(set_types)

set_from_string= set("Hoola")
print (set_from_string) #es posible combertir un str en un conjunto


set_from_tuple= set(("abc","cbv", "as", "abc")) #se pueden hacer conjuntos de tuples (las tuples van en parentesis redondos)
print(set_from_tuple)

#sets (conjuntos) a partir de una lista []

numbers=[1,2,3,1,2,3,4]
set_numbers=set(numbers)
print (set_numbers)

unique_numbers=list(set_numbers)  #se convirtió el conjunto de números que no se repiten en una lista en el conjunto numbers
print (unique_numbers)

