// Binary Tree Level Order Traversal (easy)


class Node {
    constructor(val) {
        this.val = val
        this.left = null
        this.right = null
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


// Problem Statement #
// Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.

// [[1],
// [2,3],
// [4,5,6,7]]

// example 2
// [[12],
// [7,1],
// [9,10,5]
// ] 

function traverse(root) {
    let result = []

    if (root === null) {
        return null
    }

    const queue = new Queue()
    queue.enqueue(root)

    while (queue.size > 0) {
        const queueLength = queue.size
        const currentLevel = []

        for (let i = 0; i < queueLength; i++) {
            let currentNode = queue.dequeue()

            currentLevel.push(currentNode.val);

            if (currentNode.left !== null) {
                queue.enqueue(currentNode.left)
            }

            if (currentNode.right !== null) {
                queue.enqueue(currentNode.right)
            }

        }

        result.push(currentLevel)

    }

    return result
}
// ///////////////////////// Reverse Level Order Traversal (easy) ///////////////////////////////////
// Problem Statement #
// Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest level comes first. You should populate the values of all nodes in each level from left to right in separate sub-arrays.

function traverse_reverse(root) {
    let result = []

    if (root === null) {
        return null
    }

    const queue = new Queue()
    queue.enqueue(root)

    while (queue.size > 0) {
        const queueLength = queue.size
        const currentLevel = []

        for (let i = 0; i < queueLength; i++) {
            let currentNode = queue.dequeue()

            currentLevel.push(currentNode.val);

            if (currentNode.left !== null) {
                queue.enqueue(currentNode.left)
            }

            if (currentNode.right !== null) {
                queue.enqueue(currentNode.right)
            }

        }

        console.log(currentLevel)

        result.unshift(currentLevel)
    }

    return result
}

// ///////////////////////////////////// Zigzag Traversal (medium) //////////////////////////////

// Problem Statement #
// Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.

// Example 1
function traverse_zigzag(root) {
    let result = []

    if (root === null) {
        return result
    }

    const queue = new Queue()
    queue.enqueue(root)
    let leftToRight = true

    while (queue.size > 0) {
        let queueLength = queue.size
        let currentLevel = []

        for (let i = 0; i < queueLength; i++) {
            let currentNode = queue.dequeue()

            if (leftToRight) {
                currentLevel.push(currentNode.val)
            } else {
                currentLevel.unshift(currentNode.val)
            }

            if (currentNode.left !== null) {
                queue.enqueue(currentNode.left)
            }

            if (currentNode.right !== null) {
                queue.enqueue(currentNode.right)
            }

        }

        result.push(currentLevel)
        leftToRight = !leftToRight
    }

    return result

}


// Level Averages in a Binary Tree (easy)
// Problem Statement #
// Given a binary tree, populate an array to represent the averages of all of its levels.


function find_level_average(root) {

}


function main() {
    const root = new Node(12)
    root.left = new Node(7)
    root.right = new Node(1)
    root.left.left = new Node(9)
    root.left.right = new Node(2)
    root.right.left = new Node(10)
    root.right.right = new Node(5)
    // root.right.left.left = new Node(20)
    // root.right.left.right = new Node(17)
    console.log(`Breath first transversal of a tree: ${traverse_zigzag(root)}`)

}

main()