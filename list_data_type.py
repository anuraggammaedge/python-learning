a = [1, 2, 3, 4, 5]

# print(a[0])
a.append("char")
# print(a)
a.remove(2)
a.append(5)
# print(a)

print("Index 0 Element", a[0])
print("Index 1 Element", a[1])
print("Index -1 Element", a[-1])
print("Index -2 Element", a[-2])

for nums in a:
    pass
    # print(nums)

a.insert(4, 333)
# print(a)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon"]
# print(thislist[2:5])
# print(thislist[:4])
# print(thislist[2:])
# print(thislist[::-1])  ##reverse the list

thislist[0] = "blackapple"
thislist[1:3] = ["blackcurrant", "watermelon"]

thislist.insert(2, "randomfruit")


tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)


thistuple = ("advc", "drangon fruit")
thislist.extend(thistuple)
# print(thislist)


list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_numbers = list(filter(lambda x: x%2==0, list_of_numbers))

# square = list(map(lambda x: x**2, even_numbers))

square = list(map(lambda x: x**2, filter(lambda x: x%2==0, list_of_numbers)))

# print(square)


matrix = [
    [1,2,3,4],
    [11,22,33,44],
    [111,222,333,444]
]

flat_list = []
# for list in matrix:
#     flat_list.extend(list)

# print(flat_list)

for row in matrix:
    for value in row:
        flat_list.append(value)

# print(flat_list)


matrix2 = [
    [1,2,3,4, ['a', 'b', 'c', 'd']],
    [11,22,33,44],
    [111,222,333,444]
]

nested_flat_list = []
for row in matrix2:
    for value in row:
        if isinstance(value, list):
            for val in value:   
                nested_flat_list.append(val)
        else:
            nested_flat_list.append(value)

# print(nested_flat_list)


matrix3 = [
    [1,2,3,4, ['a', 'b', 'c', 'd', ['x', 'y', 'z']]],
    [11,22,33,44],
    [111,222,333,444]
]


def flatten_list_with_extend(nested_list):
    flat_list = []
    for value in nested_list:
        if isinstance(value, list):
            result = flatten_list_with_extend(value)
            flat_list.extend(result)
        else:
            flat_list.append(value)
    return flat_listcollections

# print(flatten_list_with_extend(matrix3))

def flatten_list_with_loop(nested_list):
    flat_list = []
    for value in nested_list:
        if isinstance(value, list):
            result = flatten_list_with_loop(value)
            for val in result:
                flat_list.append(val)
        else:
            flat_list.append(value)
    return flat_list

# print(flatten_list_with_loop(matrix3))



# Custom map
def custom_map(func, list):
    new_list = []
    for val in list:
        res = func(val)
        new_list.append(res)
    return new_list

# numbers = [1, 2, 3, 4]
# squared = custom_map(lambda x: x ** 2, numbers)
# print(squared)

# custom filter
def custom_filter(func, list):
    result =[]
    for val in list:
        if func(val):
            result.append(val)
    return result


numbers = [1, 2, 3, 4]
even_numbers = custom_filter(lambda x: x if x%2==0 else None, numbers)
print(even_numbers)


from collections import Counter

ll = [11,12,13,14,15,14,13,14,12,13]
most_common = Counter(ll).most_common(3)
print('mc', most_common)



print("____________________________________")

# Use itertools.combinations to find all possible pairs from a 
# list and filter pairs that sum to a target value.

from itertools import combinations

nums_list = [1,2,3,4,5,6,4,6,2,7,8,3,6]

def combin_with_loop(data, target):
    combinations_from_list = combinations(data, 2)
    result = []
    for i in combinations_from_list:
       sum = i[0] + i[1]
       if sum == target:
           result.append(i)
    return result
            
print(combin_with_loop(nums_list, 12))

def combination_with_com(data, target):
    return [ pair for pair in combinations(data, 2) if pair[0] + pair[1] == target ]

print(combination_with_com(nums_list, 12))