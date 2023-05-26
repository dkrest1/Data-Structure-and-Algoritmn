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
graph.removeVertex("Canada");
graph.removeVertex("Nigeria");

console.log(graph);