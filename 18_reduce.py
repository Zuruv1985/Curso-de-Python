import functools 

numbers= [1, 2, 3, 4]

result= functools.reduce(lambda x,y:x+y, numbers) #functools.reduce(lambda x=Acumulador,y=valor del item:x+y, Iterador)
print (result)