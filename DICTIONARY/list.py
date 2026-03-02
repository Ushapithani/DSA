# create a dictionary by combining 2 lists 
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']
my_dict = {keys[i]: values[i] for i in range(len(keys))}
print("Combined dictionary:", my_dict)

# create a dictionary by combining 2 lists 
keys = ['name', 'age', 'city']
values = ['Bob', 25, 'Los Angeles']
combined = {}
for i in range(len(keys)):
    combined[keys[i]] = values[i]
print("Combined dictionary using loop:", combined)


# using zip 
keys = ['name', 'age', 'city']
values = ['Charlie', 35, 'Chicago']
my_dict_zip = dict(zip(keys, values))
print("Combined dictionary using zip:", my_dict_zip)