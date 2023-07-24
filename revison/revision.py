class Node:
    data = None
    next_node = None

    def __init__(self, data) -> None:
        self.data = data
    def __repr__(self) -> str:
        return "<Node: {}>".format(self.data)

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def size(self):
        current = self.head
        count = 0

        while(current):
            current = current.next_node
            count += 1
        return count

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    
    def search(self, key):
        current = self.head
        while current:
            if current.data is key:
                return current
            else:
                current = current.next_node
            return None
    def insert(self, data, index):
        new_node = Node(data)

        if index == 0:
            self.add(data)
        elif index > 0:
            position = index
            current = self.head
            node = None

            while position > 1:
                current = node.next_node
                position -= 1

                prev_node = current
                next_node = current.next_node

                prev_node.nex_node = new_node
                new_node.next_node = next_node

    def reverse(self, head):
        last = None
        while head:
            temp = head.next_node
            head.next_node = last
            last = head
            head = temp
        return last
        
            
            

