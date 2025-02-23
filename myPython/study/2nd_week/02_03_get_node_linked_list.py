class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def print_all(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def get_node(self, index):
        current = self.head
        
        for current_index in range(index):
            current = current.next
            
        return current

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(7)

print(linked_list.get_node(0).data)
print(linked_list.get_node(1).data)