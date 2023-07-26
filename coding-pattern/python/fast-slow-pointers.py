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


# //////////////////////////////////Start of LinkedList Cycle (medium) /////////////////////////////////////////////
# Problem Statement #
# Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
class Node2:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while self is not None:
            print(temp.value, end="")
            temp = temp.next
        print()

def find_cycle(head):
    cycle_length = 0
    slow, fast = head,head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        
        if slow  == fast:
            cycle_length = find_cycle_length(slow)
            break
    return find_start(head, cycle_length)

def find_cycle_length(slow):
    cycle_length = 0
    current = slow
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length
        
def find_start(head, cycle_length):
    pointer_1, pointer_2 = head, head
    while cycle_length > 0:
        pointer_2 = pointer_2.next
        cycle_length -= 1

    while pointer_1 != pointer_2:
        pointer_1 = pointer_1.next
        pointer_2 = pointer_2.next

    return pointer_1

def result_2():
    head = Node2(1)
    head.next = Node2(2)
    head.next.next = Node2(3)
    head.next.next.next = Node2(4)
    head.next.next.next.next = Node2(5)
    head.next.next.next.next.next = Node2(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start", str(find_cycle(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start", str(find_cycle(head).value))  

    head.next.next.next.next.next = head

    print("LinkedList cycle start", str(find_cycle(head).value))    

# /////////////////////////////////////////Happy Number (medium)//////////////////////////////////////////////////////

# Problem Statement #
# Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

# Example 1:

# Input: 23   
# Output: true (23 is a happy number)  
# Explanations: Here are the steps to find out that 23 is a happy number:
# 1. 2^2 + 3^2 = 4 + 9 = 13
# 2. 1^2 + 3^2 = 1 + 9 = 10
# 3. 1^2 + 0^2 = 1 (which is happy number)

# Example 2:

# Input: 12   
# Output: false (12 is not a happy number)  
# Explanations: Here are the steps to find out that 12 is not a happy number:
# 1. 1^2 + 2^2 = 1 + 4 = 5
# 2. 5^2 = 25
# 3. 2^2 + 5^2 = 4 + 25 = 29
# 4. 2^2 + 9^2 = 4 + 81 = 85
# 5. 8^2 + 5^2 = 64 + 25 = 89

# Step ‘13’ leads us back to step ‘5’ as the number becomes equal to ‘89’, this means that we can never reach ‘1’, therefore, ‘12’ is not a happy number.

def happy_number(num):
    slow, fast = num, num
    while True:
        slow = square_sum(slow)
        fast = square_sum(square_sum(fast))
        if slow == fast:
            break
    return slow == 1

def square_sum(num):
    _sum = 0

    while num > 0:
        digit = num % 10
        _sum += digit * digit
        num //= 10
    return _sum


result_3 = happy_number(1000)

def main():
    result_1()
    result_2()
    print("Happy Number: ", result_3)


main()