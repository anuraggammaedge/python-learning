class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal Constructor")

    def eat(self):
        print("Animal can eat")

    # method overriding
    def sound(self):
        print("Animal makes sound") 


    # Method Overriding + super()
    def sleep(self):
        print("Animal can sleep")


class Dog(Animal):
    def __init__(self, name, breed):
        # Calling the parent constructor
        # Call parent class method or next class in MRO (MRO - Order Python searches methods.)
        super().__init__(name) #Constructor Chaining 

        self.breed = breed

        print("Dog Constructor")

    def bark(self):
        print("Dog Bark")

    # method overriding
    def sound(self):
        print("Dog Barks method overriding")

    # Method Overriding + super()
    def sleep(self):
        super().sleep()
        print("Dog also can sleep")
    

# Multi-Level Inheritance -> puppy - dog - animal
class Puppy(Dog):

    def __init__(self):
        print("Puppy Constructor")
        super().sleep()  # Multiple Inheritance + super()
        super().bark()
        super().eat()

    def weep(self):
        print("Puppy weeps")

class Cat(Animal):
    pass

d = Dog("Tommy", "Labrador")
# d.bark()
# d.eat()
# d.sound()
# d.sleep()

# p = Puppy('jack', 'german')  #if puppy have no constructor then it will inherits the parent class constructor.
p = Puppy()

# p.eat()
# p.bark()
# p.weep()


# Method Resolution Order : 
# When you call a method, Python looks for it inside the current class first. If it is not found there, Python follows the MRO chain from left to right to find the method.
print(Cat.__mro__)



# composition over inheritance
# means : Car HAS-A Engine
class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()

# Method Overriding = Runtime Polymorphism 
# -> Same method but different behaviour = polymorphism

# Diamond Problem -> Python avoids duplicate calls using MRO.   
#       A
#     /   \
#    B     C
#     \   /
#       D   

# Encapsulation : Python doesn't enforce strict private access like Java. 

# naming convention : _name (internal use)
# Name mangling : __name  == _ClassName__name


# Python Supports Duck Typing



class A:
    pass

class B:
    pass

class W:
    pass

class C(A, B, W):
    pass


print(C.__mro__)  # first left then right classes