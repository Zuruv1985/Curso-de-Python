items = [{"product":"Camisa", "price":100},
    {"product":"pantalon", "price":300},
{"product":"pantalon_1", "price":200,}]

def add_taxes(item):
    new_item=item.copy()  #para no modificar el diccionario principal
    new_item["taxes"]= item["price"]*0.19
    return new_item

new_items=list(map(add_taxes, items))
print ("nueva lista => ", new_items)
print ("vieja lista => ", items)

