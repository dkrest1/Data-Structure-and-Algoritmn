//////IMPLEMENTING A QUEUE WITH AN ARRAY
let que = [];
que.unshift("one");
que.unshift("two");
que.unshift("three");
que.unshift("four");
// console.log(que)
que.pop();
// console.log(que)

////////////////////////////////// IMPLEMENTING QUEUE WITH LINKEDLIST
class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class Queue {
    constructor() {
        this.first = null;
        this.last = null;
        this.size = 0;
    }
    //enqueue means adding and dequeue means removing
    enqueue(val) {
        let newNode = new Node(val);
        if (!this.first) {
            this.first = newNode;
            this.last = newNode;
        } else {
            this.last.next = newNode;
            this.last = newNode;
        }
        return ++this.size;
    }

    dequeue() {
        if (!this.first) return null;
        let temp = this.first;
        if (this.first === this.last) {
            this.last = null;
        }
        this.first = this.first.next;
        this.size--;
        return temp.val;
    }
}

//BIG O
// insertion O(1)
//searching O(n)
//removal O(1)
//access O(n)

const queue = new Queue();
queue.enqueue("one");
queue.enqueue("two");
queue.enqueue("three");
// console.log(queue);
queue.dequeue();
console.log(queue);
