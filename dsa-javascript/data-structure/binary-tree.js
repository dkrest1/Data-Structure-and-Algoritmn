///////// THE BINARY TREE, BINARY SEARCH TREE, (FOR NON SORTED NODE) WE USE TREE TRAVERSAL (BREATH_FIRST_SEARCH<BFS>, AND DEPTH_FIRST_SEARCH<>DFS) 
// ORIGINAL TREE FOR BFS AND DFS
//        10
//    6        15
// 3    8        20

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

    BFS() {
        let node = this.root,
            queue = [],
            data = [];
        queue.push(node)

        while (queue.length) {
            node = queue.shift();
            data.push(node.val)
            if (node.left) queue.push(node.left)
            if (node.right) queue.push(node.right)
        }
        return data
    }

    DFSPreOrder() {
        let data = [];
        function traverse(node) {
            data.push(node.val);
            if (node.left) traverse(node.left);
            if (node.right) traverse(node.right);
        }
        traverse(this.root)
        return data;
    }

    DFSPostOrder() {
        let data = [];
        function traverse(node) {
            if (node.left) traverse(node.left);
            if (node.right) traverse(node.right);
            data.push(node.val)
        }
        traverse(this.root)
        return data;
    }

    DFSInOrder() {
        let data = [];
        function traverse(node) {
            node.left && traverse(node.left);
            data.push(node.val);
            node.right && traverse(node.right);
        }
        traverse(this.root);
        return data;
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
// tree.insert(100)
// tree.insert(90)
// tree.insert(110)
// tree.insert(80)
// tree.insert(120)
// tree.insert(130)
// // console.log(tree)
// console.log(tree.find(120));
//BFS
tree.insert(10);
tree.insert(6);
tree.insert(15);
tree.insert(3);
tree.insert(8);
tree.insert(20);
// console.log(tree.BFS())
console.log(tree.DFSPreOrder());
console.log(tree.DFSPostOrder());
console.log(tree.DFSInOrder());

