<<<<<<< HEAD
import sys

print(sys.addaudithook)
import re
text="mi numero de telefono es 87190627, el codigo de pais es 506, mi numero de la suerte es 05"

result= list(re.findall("[0-9]+", text))
print (result)

import time

timestamp= time.time
local=time.localtime()
result=time.asctime(local)
print (result)

import collections
numbers= [1,1,2,1,2,1,4,5,3,3,21]
counter=collections.Counter(numbers)
print(counter)
=======
import sys

print(sys.addaudithook)
import re
text="mi numero de telefono es 87190627, el codigo de pais es 506, mi numero de la suerte es 05"

result= list(re.findall("[0-9]+", text))
print (result)

import time

timestamp= time.time
local=time.localtime()
result=time.asctime(local)
print (result)

import collections
numbers= [1,1,2,1,2,1,4,5,3,3,21]
counter=collections.Counter(numbers)
print(counter)
>>>>>>> 2f9545c9c2433d20a64f45b71c5f66c3d994ca24
