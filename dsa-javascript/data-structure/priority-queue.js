// the data we will be working with [41, 39, 33, 18, 27, 12]
// Big O 
//insertion - O(logn)
//removal - O(logn)
//search - O(n)

class Node {
    constructor(val, priority) {
        this.val = val;
        this.priority = priority;
    }
}

class PriorityQueue {
    constructor() {
        this.value = [];
    }

    enqueue(val, priority) {
        let newNode = new Node(val, priority)
        this.value.push(newNode)
        this.bubbleUp();
    }

    bubbleUp() {
        let idx = this.value.length - 1;
        let element = this.value[idx];
        while (idx > 0) {
            let parentInx = Math.floor(idx - 1 / 2);
            let parent = this.value[parentInx];
            if (element.priority >= parent.priority) break;
            this.value[parentInx] = element;
            this.value[idx] = parent;
            idx = parentInx;
        }
    }

    dequeue() {
        let min = this.value[0];
        let end = this.value.pop();
        if (this.value.length > 0) {
            this.value[0] = end
            this.bubbleDown();
        }
        return min;
    }

    bubbleDown() {
        let idx = 0;
        let length = this.value.length;
        let element = this.value[0];
        while (true) {
            let leftChildIndex = 2 * idx + 1;
            let rightChildIndex = 2 * idx + 2;
            let leftChild, rightChild;
            let swap = null;
            if (leftChildIndex < length) {
                leftChild = this.value[leftChildIndex];
                if (leftChild.priority < element.priority) {
                    swap = leftChildIndex
                }
            }

            if (rightChildIndex < length) {
                rightChild = this.value[rightChildIndex];
                if (
                    (swap === null && rightChild.priority < element.priority) ||
                    (swap !== null & rightChild.priority < leftChild.priority)
                ) {
                    swap = rightChildIndex
                }
            }

            if (swap === null) break;
            this.value[idx] = this.value[swap];
            this.value[swap] = element;
            idx = swap
        }
    }
}

let emergency = new PriorityQueue();
emergency.enqueue("common cold", 5);
emergency.enqueue("gun shot ", 1);
emergency.enqueue("high fever", 3);
console.log(emergency);
emergency.dequeue();
console.log(emergency);