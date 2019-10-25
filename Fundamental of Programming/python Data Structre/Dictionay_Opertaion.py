'''
Dictionary ----
Dictionary is Key Value Pair.
Dictionary is Unorderd Collection of items.
'''


# 1. Data Access
dict1 = {"name":"Srk","age":20,"Address":"Indra_Nagar"}

print(dict1["name"])     # Srk
print(dict1.get("age"))  # 20

# 2. How To Add Element in Dictionary

dict1["GirlFreind"] = "Namrata"
print(dict1)   # {'name': 'Srk', 'age': 20, 'Address': 'Indra_Nagar', 'GirlFreind': 'Namrata'}

# 3. View Items in dictionary in diffrent form
print(dict1.items())   #dict_items([('name', 'Srk'), ('age', 20), ('Address', 'Indra_Nagar'), ('GirlFreind', 'Namrata')])
print(dict1.keys())    # dict_keys(['name', 'age', 'Address', 'GirlFreind'])
print(dict1.values())    # dict_values(['Srk', 20, 'Indra_Nagar', 'Namrata'])


# 4. Dictionary Comprehension

dict1 = {1:4,2:16,3:32}

for i in dict1.items():
    print(i)
    
new_dict = {2*k:v for k,v in dict1.items()}
