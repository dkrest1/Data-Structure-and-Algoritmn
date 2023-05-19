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
    push(val) {
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

    pop() {
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

    shift() {
        if (!this.head) return undefined;
        let currenthead = this.head;
        this.head = currenthead.next;
        this.length--;
        if (this.length === 0) {
            this.tail === null
        }
        return currenthead;
    }

    unshift(val) {
        let newNode = new Node(val)
        if (!this.head) {
            this.head = newNode;
            this.tail = this.head;
        } else {
            newNode.next = this.head;
            this.head = newNode;

        }
        this.length++;
        return this
    }

    get(index) {
        if (index < 0 || index >= this.length) return null;

        let counter = 0;
        let current = this.head;
        while (counter !== index) {
            current = current.next;
            counter++
        }
        return current
    }

    set(index, val) {
        let foundVal = this.get(index);
        if (foundVal) {
            foundVal.val = val;
            return true
        }

        return false;
    }

    insert(index, val) {
        if (index < 0 || index > this.length) return false;
        if (index === this.length) {
            this.push(val)
            return true;
        }

        if (index === 0) {
            this.unshift(val)
            return true;
        }

        let newNode = new Node(val);
        let prev = this.get(index - 1);
        let temp = prev.next;
        prev.next = newNode;
        newNode.next = temp;
        this.length++
        return true;
    }

    remove(index) {
        if (index < 0 || index >= this.length) return undefined;
        if (index === 0) {
            this.shift(index);
            return true
        }

        if (index === this.length - 1) {
            this.pop(index);
            return true
        }

        let prevNode = this.get(index - 1);
        let removedNode = prevNode.next;
        prevNode.next = removedNode.next;
        this.length--;
        return removedNode;
    }

    reverse() {
        let node = this.head;
        this.head = this.tail;
        this.tail = node;
        let next;
        let prev = null;
        for (let i = 0; i < this.length; i++) {
            next = node.next;
            node.next = prev;
            prev = node;
            node = next;
        }
        return this;
    }
}

//BIG O
// insertion O(1)
//searching O(n)
//removal O(1)
//access O(n)

const result1 = new SinglyLinkedList()
result1.push("hello");
result1.push("boy");
result1.push("and");
result1.push("girl");
// result1.pop();
// result1.pop();
// result1.shift();
// result1.shift();
// result1.unshift("I am the new head");
// console.log("get index ", result1.get(3))
// console.log('set val', result1.set(1, "boys"))
// console.log('set val', result1.set(3, "girls"))
// console.log('Insert Val', result1.insert(0, "We did it!"))
// console.log("removed node ", result1.remove(3))
console.log("reverse node", result1.reverse());
console.log("result1 ", result1);