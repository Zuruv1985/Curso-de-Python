# filter filtra una lista para que pertenescan a una nueva lista

numbers= [1,2,3,4,5]
new_numbers=(list(filter(lambda x: x % 2 == 0, numbers)))
print(new_numbers)
