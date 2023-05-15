
class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return "<Node: {}>".format(self.data)


class Linkedlist:

    def __init__(self) -> None:
        self.head = None

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    # it has O(n)
    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    # it has O(n)
    def search(self, key):
        current = self.head

        while current:
            if current.data is key:
                return current
            else:
                current = current.next_node
        return None

    # it has O(1)
    def insert(self, data, index):
        new_node = Node(data)

        if index == 0:
            self.add(data)

        elif index > 0:
            current = self.head
            position = index
            node = None

            while position > 1:
                current = node.next_node
                position -= 1

                prev_node = current
                next_node = current.next_node

                prev_node.next_node = new_node
                new_node.next_node = next_node

    def reverse(self, head):
        last = None
        while head:
            temp = head.next_node
            head.next_node = last
            last = head
            head = temp
        return last

    def insertBefore(self, data, node):
        current = self.head
        previous = None
        newNode = Node(data)

        while current:
            if current.data is node and current is self.head:
                self.add(data)
                break
            elif current.data is node:
                newNode.next_node = current
                previous.next_node = newNode
                break
            else:
                previous = current
                current = current.next_node

    def insertAfter(self, data, x):
        p = self.head
        while p is not None:
            if p.data == x:
                break
        p = p.next_node

        if p is None:
            print(x, "not present in the list")
        else:
            temp = Node(data)
            temp.next_node = p.next_node
            p.next_node = temp

    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current and key is not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node

            elif current.data == key:
                found = True
                current = current.next_node
                previous.next_node = current

            else:
                previous = current
                current = current.next_node

    def node_at_index(self, index):

        if index == 0:
            return self.head

        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1
            return current

    def node_at_index2(self, index):
        current = self.head
        position = 0

        while current.next_node and position < index:
            current = current.next_node
            position += 1

        if current.next_node is None and position < index:
            return "index not in list"
        else:
            return current.data

    def __repr__(self) -> str:
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: {}]".format(current.data))
            elif current.next_node is None:
                nodes.append("[Tail: {}]".format(current.data))
            else:
                nodes.append("[{}]".format(current.data))
            current = current.next_node

        return " --> ".join(nodes)

        1, 2, 3, 4, 5, 6, 7, 8


l = Linkedlist()
l.add(3)
l.add(4)
l.add(5)
l.add(9)


# print(l)
# print(l.head)
# print(l.reverse(l.head))

#l.insert(20, 1)
# print(l.__repr__())
# print(l.node_at_index(2))

a = 1
if a != 1:
    print(True)

###########################################################################################################