# lambda

x = lambda a : a + 10

print(x(10))

y = lambda a, b, c : (a+b)*c
print(y(2,3,4))

def myFunc(n):
    return lambda a : a * n

rFunc = myFunc(5)

print(rFunc(10))


nums = [1,2,3,4,5,6,7,8,9]
double = list(map(lambda a : a * 2, nums))

print(double)

square = list(map(lambda x : x ** 2, nums))
print(square)


odd_numbers = list(filter(lambda x : x % 2 != 0, nums))
print(odd_numbers)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)