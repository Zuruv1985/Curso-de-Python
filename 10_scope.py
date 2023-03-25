price = 100   #variable local

def increment():
    price = 200
    price = price + 10
    print (price)
    return price
print (price)
price_2= increment()
print (price_2)