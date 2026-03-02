# create a doctionary order and item using loop 
order = {}
for i in range(1, 6):
    item = input("Enter the name of the item: ")
    quantity = int(input("Enter the quantity of the item: "))
    order[item] = quantity
print("The order is:")
for item, quantity in order.items():
    print(f"{item}: {quantity}")




# update a new key value pair as cost item  and then retrieve all the keys from the dictionary
order['cost'] = 100
print("The updated order is:")
for item, quantity in order.items():
    print(f"{item}: {quantity}")

# retrieve all the keys from the dictionary
print("The keys in the order dictionary are:")
for key in order.keys():
    print(key)