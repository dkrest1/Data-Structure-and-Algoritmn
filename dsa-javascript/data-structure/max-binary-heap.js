// the data we will be working with [41, 39, 33, 18, 27, 12]

class MaxBinaryheap {
    constructor() {
        this.value = [];
    }

    insert(element) {
        this.value.push(element);
        this.bubbleUp();
    }

    bubbleUp() {
        let idx = this.value.length - 1;
        let element = this.value[idx]
        while (idx > 0) {
            let parentInx = Math.floor(idx - 1 / 2);
            let parent = this.value[parentInx];
            if (element <= parent) break;
            this.value[parentInx] = element;
            this.value[idx] = parent;
            idx = parentInx;
        }
    }

    extractMax() {
        let max = this.value[0];
        let end = this.value.pop();
        if (this.value.length > 0) {
            this.value[0] = end
            this.bubbleDown();
        }
        return max
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
                if (leftChild > element) {
                    swap = leftChildIndex
                }
            }

            if (rightChildIndex < length) {
                rightChild = this.value[rightChildIndex];
                if (
                    (swap === null && rightChild > element) ||
                    (swap !== null & rightChild > leftChild)
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
// [41, 39, 33, 18, 27, 12]
let heap = new MaxBinaryheap();
heap.insert(41);
heap.insert(39);
heap.insert(33);
heap.insert(18);
heap.insert(27);
heap.insert(12);
heap.insert(55);
heap.insert(1000);
console.log(heap)
console.log(heap.extractMax())
console.log(heap.extractMax())
console.log(heap.extractMax())
console.log(heap);