
#generar lista de numeros del 1 al 10 

"""numbers=[]

for element in range (1,11):

    numbers.append(element)

print (numbers)

#generar lista de numeros del 1 al 10 con list comprehensions

numbers_v2=[element for element in range (1,11)]  #el primer elemento es el que estará incluido en el conjunto generado
print (numbers_v2)


#la misma pero generado multiplicado por 2

numbersv3=[]

for elemen in range (1,11):

    numbersv3.append(elemen*2)

print (numbersv3)


numbers_v3=[element*2 for element in range (1,11)]  #el primer elemento es el que estará incluido en el conjunto generado
print (numbers_v3)
"""

#COn condicional
numbers=[]

for i in range (1,11):
    if i % 2==0:
        numbers.append(i*2)
print (numbers)

numbers_v2=[i*2 for i in range (1,11) if i % 2 ==0 ]
print (numbers_v2)

