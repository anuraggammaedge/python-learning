class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def print_stack(self):
        for item in self.items[::-1]:
            print(f"|{item}|")
    

my_stack  = Stack()

my_stack.push(11)
my_stack.push(12)
my_stack.push(13)
my_stack.push(14)
my_stack.pop()

print(my_stack.peek())
my_stack.print_stack()