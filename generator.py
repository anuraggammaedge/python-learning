#  Generator is a special type of function in python that produce values lazily instead of returning everything at once.
# Internal Working ->
# generator:
    # 1. pause execution
    # 2. preserve state 
    # 3. resume later

# StopIteration : when next() on generator is called and there are no more items to yield, 
# it raises StopIteration exception to signal that the generator is exhausted. This is how the for loop knows when to stop iterating over a generator.

def numbers():
    yield 1
    yield 2
    yield 3

# print(numbers())  # generator does not execute immediately. -> returns reference = <generator object numbers at 0x74db54b84a90>
gen_obj = numbers()
# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))

# yield : turns a function into generator.


for num in numbers():
    # print(num)
    pass


# Execution flow

def test():
    print("before first yield 1")
    yield 1


    print("after first yield 1")
    print("before second yield 2")
    yield 2

    print("after second yield 2")

gen = test()

# print(next(gen))
# print(next(gen))


# Generator Expression

nums = (x for x in range(10000))
# print(nums)
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))

# yield from - advance generator delegation.

def sub():
    yield 1
    yield 2

def main():
    yield from sub()
    yield 3

for x in main():
    # print(x)
    pass


# Genertor pipeline pattern


def read_data():
    for i in range(10):
        print(i)
        yield i

def filter_even(data):
    for num in data:
        if num % 2 == 0:
            print(num)
            yield num

def square(data):
    for item in data:
        print(item)
        yield item * item

elt_pipeline = square(
    filter_even(
        read_data()
    )
)

for value in elt_pipeline:
    print(value)

# Write a generator function that yields Fibonacci numbers up to n.

# Difference between return and yield?
# return	                yield
# terminates function	    pauses function
# returns one value	        produces sequence lazily


# Difference between iterator and generator?

# Generator is a simpler way to create iterators.