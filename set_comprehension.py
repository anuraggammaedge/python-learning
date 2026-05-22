# {
#     expression
#     for item in iterable
# }

numbers = {
    item
    for item in range(1,10)
    if item % 2==0
}

num = {
    x % 3
    for x in range(1,11)
}

# print(num)

nums = [1, 2, -2, 3, 3, 4, -4, 5]

sq = {
    x ** 2
    for x in nums
}
# print(sq)  # duplicate removed

#  Vowel Extractor
sentence = "hello world python programming"
vowel = ['a', 'e', 'i', 'o', 'u']

vowel_ex = {
    x.lower() 
    for x in sentence
    if x in vowel
}
# print(vowel_ex)


# Length Bound Words
words = ["apple", "bat", "car", "banana", "kiwi", "egg", "apple"]

upper_words = {
    x.upper()
    for x in words
    if len(x) > 3
}
# print(upper_words)


# 
amounts = [500, -20, 1000, -50, -20, 500, -100]
negative_trans = {
    # num * -1 if  num < 0 else num * 1
    # -num
    abs(num)
    for num in amounts 
    if num < 0
}
print(negative_trans)

# Flattening : Grid DataGiven a nested matrix with duplicate data:
matrix = [
    [1, 2, 3, 2],
    [4, 3, 5, 1],
    [2, 6, 4, 3]
]
flatten_list = {
    num
    for row in matrix 
    for num in row
}
print(flatten_list)




# nested comprehension
matrix1 = [
    [[y for y in range(3) ]for x in range(3) ]
    for _ in range(3)
]
print(matrix1)
