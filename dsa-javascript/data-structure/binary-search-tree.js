///////// THE BINARY SEARCH TREE
class Node {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class binarySearchTree {
    constructor() {
        this.root = null;
    }

    insert(val) {
        let newNode = new Node(val);
        if (this.root === null) {
            this.root = newNode;
            return this
        }

        let current = this.root;
        while (true) {
            if (val === current.val) return undefined;
            if (val < current.val) {
                if (current.left === null) {
                    current.left = newNode;
                    return this
                }
                current = current.left
            } else if (val > current.val) {
                if (current.right === null) {
                    current.right = newNode;
                    return this
                }
                current = current.right;
            }
        }
    }

    find(val) {
        if (this.root === null) return false;
        let current = this.root;
        let found = false;
        while (current && !found) {
            if (val < current.val) {
                current = current.left;
            } else if (val > current.val) {
                current = current.right
            } else {
                found = true
                return found
            }
        }
        return false
    }
}

//BIG O
//insertion - O(log n)
//searching - O(log n)

const tree = new binarySearchTree();
// tree.root = new Node(10);
// tree.root.right = new Node(20);
// tree.root.left = new Node(5);
// tree.root.right.right = new Node(30);
// console.log(tree)
tree.insert(100)
tree.insert(90)
tree.insert(110)
tree.insert(80)
tree.insert(120)
tree.insert(130)
// console.log(tree)
console.log(tree.find(120));

