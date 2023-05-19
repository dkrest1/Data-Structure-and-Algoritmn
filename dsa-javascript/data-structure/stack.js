//let say we are using javascript in built array and we are storing browsing history
let stack = [];
stack.push("twitter");
stack.push("linkedin");
stack.push("facebook");
stack.pop();
stack.pop();
// console.log(stack);

////////////////// IMPLEMENTATION OF STACK WITH LINKED LIST {SHIFT AND UNSHIFT}
class Node {
    constructor(val) {
        this.val = val;
        this.next = null
    }
}

class Stack {
    constructor() {
        this.first = null;
        this.last = null;
        this.size = 0
    }

    push(val) {
        let newNode = new Node(val);
        if (this.length === 0 || !this.first) {
            this.first = newNode;
            this.last = newNode;
        } else {
            let temp = this.first;
            this.first = newNode;
            this.first.next = temp;
        }
        return ++this.size;
    }

    pop() {
        if (!this.first) return null;
        let temp = this.first;
        if (this.first === this.last) {
            this.last === null;
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

let result = new Stack();
result.push("one");
result.push("two");
result.push("three");
result.push("four");
result.pop();
result.pop();
console.log(result);