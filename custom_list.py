class CustomList:
    def __init__(self):
        self.item = []

    def __getitem__(self, index):
        return self.item[index]

    def __setitem__(self, index, value):
        self.item[index] = value

    def __len__(self):
        return len(self.item)
    
    def append(self, value):
        self.item.append(value)

    def __repr__(self):
        return f"custom list {self.item}"

numbers = CustomList()

numbers.append(10)
numbers.append(20)
numbers.append(30)
numbers.append(40)

print(numbers)  # repr 

print(numbers[3])   #get
numbers[3] = 99  #set
print(numbers[3])

print(len(numbers))