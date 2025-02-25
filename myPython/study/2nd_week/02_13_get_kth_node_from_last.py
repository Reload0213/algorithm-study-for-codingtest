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

    def get_kth_node_from_last(self, k):
        length = 1
        current = self.head
        
        while current.next is not None:     
            current = current.next
            length += 1
       
        current = self.head
        target_index = length - k
       
        for index in range(target_index):
            current = current.next
        return current
    
        # 포인터를 두개 두고 시작하는 방법
        # 하지만 그닥 차이 없음음
        # slow = self.head
        # fast = self.head

        # for i in range(k):
        #     fast = fast.next

        # while fast is not None:
        #     slow = slow.next
        #     fast = fast.next

        # return slow
            
linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!