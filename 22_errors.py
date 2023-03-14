<<<<<<< HEAD
"""
try:
    print (0/0)
except ZeroDivisionError as error:
    print (error)
try:
    assert 1!=1, "uno no es diferente que uno"
except AssertionError as error:
    print(error)
try:
    age= 10
    if age<18:
        raise Exception("No eres mayor de edad, lo siento, no puedes continuar")    
except Exception as error:
    print (error)
"""
try: #un try con varias excepciones

    print (0/0)
    assert 1!=1, "uno no es diferente que uno"
    age= 10
    if age<18:
        raise Exception("No eres mayor de edad, lo siento, no puedes continuar")   


except ZeroDivisionError as error:
    print (error)
except AssertionError as error:
    print(error)
except Exception as error:
    print (error)

print("Hola")


=======
"""
try:
    print (0/0)
except ZeroDivisionError as error:
    print (error)
try:
    assert 1!=1, "uno no es diferente que uno"
except AssertionError as error:
    print(error)
try:
    age= 10
    if age<18:
        raise Exception("No eres mayor de edad, lo siento, no puedes continuar")    
except Exception as error:
    print (error)
"""
try: #un try con varias excepciones

    print (0/0)
    assert 1!=1, "uno no es diferente que uno"
    age= 10
    if age<18:
        raise Exception("No eres mayor de edad, lo siento, no puedes continuar")   


except ZeroDivisionError as error:
    print (error)
except AssertionError as error:
    print(error)
except Exception as error:
    print (error)

print("Hola")


>>>>>>> 2f9545c9c2433d20a64f45b71c5f66c3d994ca24
