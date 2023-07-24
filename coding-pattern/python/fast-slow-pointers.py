# Introduction
# The Fast & Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two pointers which move through the array (or sequence/LinkedList) at different speeds. This approach is quite useful when dealing with cyclic LinkedLists or arrays.

# By moving at different speeds (say, in a cyclic LinkedList), the algorithm proves that the two pointers are bound to meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.

# One of the famous problems solved using this technique was Finding a cycle in a LinkedList. Let’s jump onto this problem to understand the Fast & Slow pattern.


#/////////////////////////// LinkedList Cycle (easy) ////////////////////////////////////
# Problem Statement #
# Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.

#defining the node
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:

            # Similar Problems #
            # Problem 1: Given the head of a LinkedList with a cycle, find the length of the cycle.

            # Solution: We can use the above solution to find the cycle in the LinkedList. Once the fast and slow pointers meet, we can save the slow pointer and iterate the whole cycle with another pointer until we see the slow pointer again to find the length of the cycle.

            # Here is what our algorithm will look like:

            return True, cycle_length(slow)
                 
    return False

def cycle_length(slow):
    current = slow
    circle_lenght_count = 0
    while True:
        current = current.next
        circle_lenght_count += 1
        if current == slow:
            break
    return circle_lenght_count


def result_1():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle", str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("linkedList has cycle and cycle count is", str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle and cycle count is", str(has_cycle(head)))


def main():
    result_1()

    

main()