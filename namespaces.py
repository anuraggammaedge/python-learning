# Namespace - a mapping between the names and objects

x = 100  # _> global
# x -> name 
# 10 -> object 

# Namespaces types:
# 1. local  -> inside a function
# 2. global -> inside a module 
# 3. built-in -> python built-ins

# LEGB rule: left to right
# Local -> enclosing scope -> global -> built-in  

def test():
    y =10  # -> local
    print(y)

# test()   
# Y exists only inside the function  -> local
# print(y)

def show():
    print(x)
    # Function accesses global variable.

# show()

# ----------------------------------------------


x = 'global'

def outer():
    x = 'enclosing'

    def inner():
        x = 'local'
        print(x)

    inner()

outer() # output -> local


# -----------------------------------
# global Keyword
count = 0 
def increment():
    global count
    count += 1

increment()

print(count)


def outer_func():
    count = 0

    def inner_func():
        nonlocal count  # 1. It only searches nesting functions. it cannot access global varibale `use global keyword`
                        # 2. The variable must already be defined in the outer function. You cannot use nonlocal to create a brand new variable.
        count += 1
        print(f'inner {count}')

    inner_func()
    print(f'outer {count}')

outer_func()