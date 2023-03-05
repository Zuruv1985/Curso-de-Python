"""
dict= {}

for i in range (1,11):
    dict[i]=i*2
    
print (dict)

dict_v2={i:i*2 for i in range (1,11)}

print (dict_v2)

import random
countries=["col","mex", "bol", "pe"]  #una lista y generar un diccionario
population={}

for country in countries:
    population [country]=random.randint(1,100)

print (population)

population_v2={country:random.randint(1,100) for country in countries}

print (population_v2)
"""

names= ["Nico", "Zule", "Santi"]
Ages= [12, 56, 98]
print (list(zip(names, Ages)))

new_dic={name: Age for (name,Age) in zip(names,Ages) }
print (new_dic)
