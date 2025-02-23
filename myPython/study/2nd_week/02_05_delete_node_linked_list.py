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
    
    def add_node(self, index, value):
        new_node = Node(value)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            
        
        # next의 값에 value를 넣어줘야하기 때문에 index - 1번째를 찾아준 후
        prev_node = self.get_node(index - 1)
        
        # 새로운 값을 넣어주기전 다음 값을 먼저 보관 해두고고
        origin_next_node = prev_node.next

        # 새로운 값을 next에 삽입
        prev_node.next = new_node
        
        # 기존 next값을 새로운 값 이후에 바로 삽입입
        new_node.next = origin_next_node
                
    def delete_node(self, index):
        if index == 0:
            self.head =  self.head.next

        prev_node = self.get_node(index - 1)
        index_node = self.get_node(index)

        prev_node.next = index_node.next

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(7)
linked_list.append(8)

linked_list.delete_node(1)

linked_list.print_all()
