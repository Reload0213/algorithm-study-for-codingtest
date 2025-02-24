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

    def get_number(self):
        current = self.head
        calculated_number = 0
        
        while current is not None:
            calculated_number = calculated_number * 10 + current.data 
            current = current.next
            
        return calculated_number


def get_linked_list_sum(linked_list_1, linked_list_2):
    linked_list1_num = linked_list_1.get_number()
    linked_list2_num = linked_list_2.get_number()
    
    return linked_list1_num + linked_list2_num


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))