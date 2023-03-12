# print (0/0) = ZeroDivisionError
#print(result) #nameError

suma=lambda x,y:x+y

assert suma (2,2) == 4 #asert resuelve de forma correcta para verificar si una función funciona como deberia

age=10

if age<18:
    raise Exception("lo siento, no puedes continuar") # se genera una esepción para termianr el programa