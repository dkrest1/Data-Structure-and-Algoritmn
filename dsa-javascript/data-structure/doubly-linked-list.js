class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}

class DoublyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    push(val) {
        let newNode = new Node(val);
        if (this.length === 0) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode;
            newNode.prev = this.tail;
            this.tail = newNode;
        }
        this.length++
        return this
    }

    pop() {
        if (!this.head) return undefined;
        let popped = this.tail;
        if (this.length === 1) {
            this.head = null;
            this.tail = null;
        } else {
            this.tail = popped.prev;
            this.tail.next = null;
            popped.prev = null;
        }

        this.length--
        return this
    }

    shift() {
        if (this.length === 0) return undefined;
        let oldHead = this.head;
        if (this.length === 1) {
            this.head = null;
            this.tail = null;
        } else {
            this.head = oldHead.next;
            this.head.prev = null;
            oldHead.next = null
        }

        this.length--;
        return oldHead

    }

    unshift(val) {
        if (this.length === 0) return undefined;

        let newNode = new Node(val);
        if (this.length === 1) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.head.prev = newNode;
            newNode.next = this.head;
            this.head = newNode;
        }

        this.length++
        return this;
    }

    get(index) {
        if (index < 0 || index >= this.length) return null;
        if (index <= this.length / 2) {
            console.log('counting from the start!')
            let count = 0;
            let current = this.head;
            while (count !== index) {
                current = current.next;
                count++;
            }
            return current;
        } else {
            console.log('counting from the end!')
            let count = this.length;
            let current = this.tail;
            while (count !== index) {
                current = current.prev;
                count--;
            }
            return current;
        }
    }

    set(index, val) {
        let found = this.get(index);
        if (found !== null) {
            found.val = val;
            return true;
        }

        return false;
    }

    insert(index, val) {
        if (index < 0 || index > this.length) return false;
        if (index === 0) {
            this.unshift(val);
            return true
        }
        if (index === this.length - 1) {
            this.push(val);
            return true;
        }

        let newNode = new Node(val);
        let beforeNode = this.get(index - 1);
        let afterNode = beforeNode.next;
        beforeNode.next = newNode;
        newNode.prev = beforeNode;
        afterNode.prev = newNode
        newNode.next = afterNode;
        this.length++
        return true;
    }

    remove(index) {
        if (index < 0 || index >= this.length) return undefined;
        if (index === 0) {
            this.shift();
            return true
        }
        if (index === this.length - 1) {
            this.pop()
            return true
        }

        let removed = this.get(index - 1);
        removed.prev.next = removed.next;
        removed.next.prev = removed.prev;
        removed.next = null;
        removed.prev = null;
        return true
    }
}

//BIG O
// insertion O(1)
//searching O(n)
//removal O(1)
//access O(n)

const list = new Node("one");
list.next = new Node("two");
// list.next.prev = list;
const val = new DoublyLinkedList('val')
val.push("one")
val.push("two")
val.push("three")
val.push("four")
val.push("five")
val.push("six")
// val.pop();
// val.shift()
// val.unshift("zero");
// console.log('GET VALUE ', val.get(5))
// console.log('SET VALUE ', val.set(5, "seven"))
// console.log('INSERT VALUE ', val.insert(6, "seven"))
console.log('REMOVE VALUE ', val.remove(5))
console.log(val)
