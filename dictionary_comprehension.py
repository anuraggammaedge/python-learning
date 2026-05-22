# basic syntax 
# {
#     key_expression: value_expression
#     for item in iterable
# }


square = {
    x : x **2
    for x in range(10,1, -1)
}
print(square)


condition_in_dict = {
    x : x** 2
    for x in range(1,10)
    if x % 2==0
}
print(condition_in_dict)

# Swaping key/value in dict

data ={
    "name": "Anurag",
    "role": "Engineer"
}
swapped = {
    value: key 
    for key, value in data.items()
}
print(swapped)


# condition expression on vales of dict

even_odd_dict = {
    x : "even" if x % 2 == 0 else "odd"
    for x in range(1,11)
}
print(even_odd_dict)


# Merging and filtering

keys = ['apple', 'banana', 'cherry']
prices = [120, 60, 250]

exp_cal ={
    k:v
    for k,v in zip(keys, prices)
    if v > 100
}
print(exp_cal)

# Merging or Updating Existing Dictionaries

old_prices = {'laptop': 1000, 'mouse': 50, 'monitor': 300}

new_prices ={
    k:round(v * 1.1)
    for k,v in old_prices.items()
}

print(new_prices)

# Handling Duplicate Keys During Swapping
roles = {"Anurag": "Engineer", "Rahul": "Engineer", "Amit": "Manager"}

grouped_roles = {
    role : [name for name, r in roles.items() if r == role]
    for role in set(roles.values())
}

print(grouped_roles)