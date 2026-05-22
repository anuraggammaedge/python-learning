import requests
import dis

# print('first python code')
# print(requests.__version__)

def func(a, b):
    return a + b

dis.dis(func)

def foo(): pass
print(type(foo))
print(foo.__code__)
print(foo.__globals__)