<<<<<<< HEAD
item = [{"product":"Camisa", "price":100},
    {"product":"pantalon", "price":300},
{"product":"pantalon_1", "price":200,}]

prices=list(map(lambda item:item["price"], item))
print (prices)
products=list(map(lambda items:items["product"], item))
print (products)

def add_taxes(item):
    item["taxes"]= item["price"]*0.19
    return item

new_items=list(map(add_taxes, item))
=======
item = [{"product":"Camisa", "price":100},
    {"product":"pantalon", "price":300},
{"product":"pantalon_1", "price":200,}]

prices=list(map(lambda item:item["price"], item))
print (prices)
products=list(map(lambda items:items["product"], item))
print (products)

def add_taxes(item):
    item["taxes"]= item["price"]*0.19
    return item

new_items=list(map(add_taxes, item))
>>>>>>> 2f9545c9c2433d20a64f45b71c5f66c3d994ca24
print (new_items)