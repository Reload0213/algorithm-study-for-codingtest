class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# first_node = Node(5)
# second_node = Node(12)

# first_node.next = second_node

# third_node = Node(7)
# second_node.next = third_node

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        
    def append(self, value):
        current = self.head
        
        while current.next != None:
            current = current.next
        
        current.next = Node(value)
    
    def print_all(self):
        current = self.head
        
        while current != None:
            print(current.data) 
            current = current.next

linked_list = LinkedList(5)

linked_list.append(12)

linked_list.append(8)
linked_list.append(11)

linked_list.print_all()