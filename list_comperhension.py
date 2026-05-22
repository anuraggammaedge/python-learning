numbers  = []
for i in range(6):
    numbers.append(i)

nums = [x for x in range(6)] # list comperhension

# Square
sq = [x*x for x in range(6)]
print(sq)


# use for Filtering
sq_with_condition = [x*x for x in range(6) if x % 2 == 0]
print(sq_with_condition)

# use for transformation
# codition_expression = [tru_value if condition else false_value for item in iterable]
labels = ["Even" if x%2==0 else "Odd" for x in range(10)]
print(labels)


# Nested list comperhension

matrix = [
    [1,2,3],
    [4,5,6]
]

flatten_list = [num for row in matrix for num in row]
print(flatten_list)

nested_matrix = [
    [1,2,3, ['a', 'b', 'c']],
    [4,5,6]
]

flatten_nested_list = [val for inner_list in nested_matrix for item_or_list in inner_list for val in (item_or_list if isinstance(item_or_list, list) else [item_or_list])]
# print(flatten_nested_list)

lm_matrix = [
    [1, 2, 3, ['a', 'b', ['deep_1', 'deep_2', ['deepest-1', 'deepest-4']]]], # 3 layers deep
    [4, 5, 6]
]
lambda_flatten = lambda lm :[val for item in lm for val in (lambda_flatten(item) if isinstance(item, list) else [item]) ] 
print(lambda_flatten(lm_matrix))


# Multiple Conditions

# it is AND condition
nums_mutiple_condition = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
print(nums_mutiple_condition)

nums_mutiple_condition_OR = [x for x in range(20) if x % 2 == 0 or x % 3 == 0]
print(nums_mutiple_condition_OR)


# function call in compenhension
names = ['anurag', 'python']

capitalized = [name.upper() for name in names]
print(capitalized)

# Transformation

data = [1,2,3,4]

result = [
    {
        'number': x,
        'square': x**2,
        'cube': x**3
    }
    for x in data
]
print(result)