# Exception is an event that interrupts normal program execution. 
# (exception - Recoverable runtime issue.)
# (error - serious system issue)

# BaseException - catches keyboardInterrupt and systemexit.



# raise -> Preserve original traceback (always use raise first)
# raise e -> Resets traceback 


# 1. ZeroDivisionError : division by zero.
# print(10 / 0)

try: 
    print(10 / 0)

except ZeroDivisionError:
    print('Cannot division by zero.')


# 2. ValueError

# data = int(input("Enter number: "))
# print(data * 10)  # if user enter 'abc' program fails and throw valueError.

try:
    data = int(input("Enter number: "))
    print(data * 10)  
except ValueError:
    print("Invalid number")



# 3. Catching Multiple Exceptions

# 3.1 mutiple except blocks

try:
    num = int(input("Enter Numbers:"))
    result = 10 / num

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot division by zero.")

# 3.2 Tuple of exceptions

try:
    num = int(input("Enter Numbers:"))
    result = 10 / num

except(ValueError , ZeroDivisionError ) as e:
    print("Invalid Number", e)

# 4. Generic Exception handling.

try:
    num = int(input("Enter Numbers:"))
    result = 10 / num

except Exception as e:
    print("Error: " , e)

# 5. else block with exception.
try:
    num = int(1)

except ValueError:
    print("Invalid Number")

else:
    # run only if no exception occurs.
    # Use else for:
        # database commits
        # success logging

    print("Conversion Successfully")

# 6. Finally block - runs always

try:
    print("Try block")
    result = 10 / 2

except ZeroDivisionError:
    print("Except block")

else:
    print("Else block")

finally:
    #use when :
        # DB connection cleanup
        # file closing
        # socket closing
    print("Finally block")

# 7. Raising Exceptions -  we can manually raise exceptions with raise in any program.
age = -5

# if age < 0:
#     raise ValueError("Age cannot be negative")



# Exception Chaining - chain a mutiple exception in except block.
try:
    int(1)
except ValueError as e:
    raise RuntimeError("conversion falied") from e


# 8. Common built-in exception.
    # 1. ValueError - wrong value type or content
    # 2. TypeError - Wrong datatype operation -> eg : '10' + 5
    # 3. IndexError - index not found in given lit
    # 4. KeyError - key not found in given dict.
    # 5. FileNotFoundError - file is not exist.
    # 6. ZeroDivisionError - when we try to divide any number with zero.
    # 7. AttributeError - This happens when you try to call a method or access a variable (an attribute) that does not exist for that specific data type or object.
    # 8. ImportError / ModuleNotFoundError - wrong import or package is not installed.
    # 9. RuntimeError - genric runtime error.
    # 10. AssertionError - the assert keyword is used as a debugging tool to test if a condition is True. If the condition is True, the code moves on normally. If the condition is False, Python immediately stops the program and raises an AssertionError.

# Assertion example
x = 5
assert x == 10, "x is not equal to 10"

# Context Managers -  **with internally uses exception handling.