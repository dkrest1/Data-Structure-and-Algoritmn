// we will first be building an unidirected graph
class Graph {
    constructor() {
        this.adjancencyList = {};
    }
    //adding a vertex
    addVertex(vertex) {
        if (!this.adjancencyList[vertex]) this.adjancencyList[vertex] = [];
    }
    //adding edge to our graph
    addEdge(vertex1, vertex2) {
        this.adjancencyList[vertex1].push(vertex2);
        this.adjancencyList[vertex2].push(vertex1);
    }
    removeEdge(vertex1, vertex2) {
        this.adjancencyList[vertex1] = this.adjancencyList[vertex1].filter(vertex => vertex !== vertex2);
        this.adjancencyList[vertex2] = this.adjancencyList[vertex2].filter(vertex => vertex !== vertex1);
    }
    removeVertex(vertex) {
        while (this.adjancencyList[vertex].length) {
            let removedVertex = this.adjancencyList[vertex].pop();
            this.removeEdge(vertex, removedVertex);
        }
        delete this.adjancencyList[vertex]
    }

    depthFirstRecursive(start) {
        let result = [];
        let visited = {};
        let adjancencyList = this.adjancencyList;
        (function dfs(vertex) {
            if (!vertex) return null;
            visited[vertex] = true;
            result.push(vertex);
            adjancencyList[vertex].forEach(neighbour => {
                if (!visited[neighbour]) {
                    return dfs(neighbour);
                }
            })
        })(start);
        return result
    }

    depthFirstIterative(start) {
        let stack = [start];
        let visited = {};
        let result = [];
        let currentVertex;
        visited[start] = true;
        while (stack.length) {
            currentVertex = stack.pop();
            result.push(currentVertex);
            this.adjancencyList[currentVertex].forEach(neighbour => {
                if (!visited[neighbour]) {
                    visited[neighbour] = true;
                    stack.push(neighbour);
                }
            })
        }
        return result;
    }

    breathFirstIterative(start) {
        let result = [];
        let visited = {};
        let currentVertex;
        let queue = [start];
        visited[start] = true;

        while (queue.length) {
            currentVertex = queue.shift();
            result.push(currentVertex);
            this.adjancencyList[currentVertex].forEach(neighbour => {
                if (!visited[neighbour]) {
                    visited[neighbour] = true;
                    queue.push(neighbour);

                }
            })
        }
        return result;

    }

}

const graph = new Graph();
graph.addVertex("Nigeria");
graph.addVertex("United Kingdom");
graph.addVertex("Canada");
graph.addEdge("United Kingdom", "Nigeria");
graph.addEdge("United Kingdom", "Canada");
graph.addEdge("Nigeria", "Canada");
// graph.removeEdge("Nigeria", "United Kingdom");
// graph.removeEdge("Canada", "Nigeria");
// graph.removeVertex("Canada");
// graph.removeVertex("Nigeria");
// console.log(graph.depthFirstIterative("Nigeria"));
// console.log(graph.depthFirstRecursive("Nigeria"));
console.log(graph.breathFirstIterative("Canada"));
// console.log(graph);