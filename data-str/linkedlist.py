class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' -> ')
            current = current.next
        print("None")

first = LinkedList()
first.append('123')
first.append('456')
first.append('789')

first.display()