// define the class
class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    // add to the singly linked list
    add(val) {
        let newNode = new Node(val);
        if (!this.head) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode;
            this.tail = newNode
        }

        this.length++
        return this
    }

    remove() {
        if (!this.head) return undefined;
        let current = this.head;
        let newTail = current;
        while (current.next) {
            newTail = current;
            current = current.next;
        }

        this.tail = newTail;
        this.tail.next = null
        this.length--
        if (this.length === 0) {
            this.head = null;
            this.tail = null
        }

        return current;
    }
}

const result1 = new SinglyLinkedList()
result1.add("hello");
result1.add("boy");
result1.add("and");
result1.add("girl");
result1.remove();
result1.remove();
result1.remove();
result1.remove();
result1.remove();
console.log("result1 ", result1);