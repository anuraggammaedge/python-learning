class CustomStack:
  def __init__(self):
    self.stack = []
    
  def push(self,val):
    self.stack.append(val)
    
  def is_empty(self):
    return len(self.stack) == 0
      
  def pop(self):
    if self.is_empty():
      return 'stack is empty'
    return self.stack.pop()
    
  def peek(self):
    if not self.is_empty():
      return self.stack[-1]
      
  def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Current Stack (Top to Bottom):")
            # We iterate in reverse to show the 'Top' of the stack first
            for item in reversed(self.stack):
                print(f"| {item} |")
            print(" --- ")
  
# if __name__ == '__main__'


str1 = '({{]}[)('
def isvalid(str1):
  
    map = {
    ')' : '(',
    ']' : '[',
    '}' : '{'
    }
    # print(map)

    my_stack = CustomStack()

    for char in str1:
        if char in map:
            if not my_stack.is_empty() and my_stack.peek() == map[char]:
                my_stack.pop() 
            else:
                return False
    else:
        my_stack.push(char)
    return True

print(isvalid(str1))