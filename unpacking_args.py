#  Unpacking arguments in Python allows you to pass a variable number of arguments to a function.
# 1. Unpacking with **kwargs - it allows us to pass a variable number of keyword arguments to a function. It collects the keyword arguments into a dictionary.
# 2. Unpacking with *args - it allows us to pass a variable number of non-keyword arguments to a function. It collects the non-keyword arguments into a tuple.

def user(name, age, value):
    print(name, age, value)

def user(**kwargs):
    print(kwargs)
    print(kwargs["name"], kwargs["age"], kwargs["value"])

data = {
    "name": "Anurag",
    "age": 25,
    "value": "some_value"
}

user(**data)


# def add(a, b, c):
#     return a + b + c

def add(*args):
    return sum(args)

values = [1, 2, 2, 4, 5]

print(add(*values))

# merge two lists

a = [1,2,3,4]
b = [11,12,13,14]

n = [*a, *b]
print(n)


# merged two dict

d1 = {"a": 1}
d2 = {"b": 2}

d3 = {**d1, **d2}
print(d3)