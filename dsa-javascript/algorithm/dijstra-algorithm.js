//dijstra-alorithm is majorly use to get the shortest distance between two nodes
//weighted graph
class PriorityQueue {
    constructor() {
        this.val = [];
    }

    enqueue(val, priority) {
        this.val.push({ val, priority })
        this.sort()
    }

    dequeue() {
        return this.val.shift()
    }

    sort() {
        this.val.sort((a, b) => a.priority - b.priority)
    }
}

class WeightedGraph {
    constructor() {
        this.adjacencyList = {};
    }

    addVertex(vertex) {
        if (!this.adjacencyList[vertex]) this.adjacencyList[vertex] = [];
    }

    addEdge(vertex1, vertex2, weight) {
        this.adjacencyList[vertex1].push({ node: vertex2, weight });
        this.adjacencyList[vertex2].push({ node: vertex1, weight })

    }


    dijkstra(start, finish) {
        let nodes = new PriorityQueue();
        let distances = {};
        let previous = {};
        let path = []; //to be return at end 
        let smallest;

        //buiding up initial state
        for (let vertex in this.adjacencyList) {
            if (vertex === start) {
                distances[vertex] = 0;
                nodes.enqueue(vertex, 0);
            } else {
                distances[vertex] = Infinity;
                nodes.enqueue(vertex, Infinity);
            }

            previous[vertex] = null;
        }

        //as long as there is something to visit 
        while (nodes.val.length) {
            smallest = nodes.dequeue().val;
            if (smallest === finish) {
                //we are done
                //build up path to return at end
                while (previous[smallest]) {
                    path.push(smallest);
                    smallest = previous[smallest]
                }
                break;
            }

            if (smallest || distances[smallest] !== Infinity) {
                for (let neighbour in this.adjacencyList[smallest]) {
                    //find up the neighbouring node 
                    let nextNode = this.adjacencyList[smallest][neighbour];
                    //calculate new distance to neighbouring node;
                    let candidate = distances[smallest] + nextNode.weight;
                    let nextNeighbour = nextNode.node;
                    if (candidate < distances[nextNeighbour]) {
                        //updating new smallest distance to neighbour
                        distances[nextNeighbour] = candidate;
                        //updating previous - how we got to neighbour
                        previous[nextNeighbour] = smallest;
                        //enqueue in priority queue with new priority
                        nodes.enqueue(nextNeighbour, candidate)
                    }
                }
            }
        }
        return path.concat(smallest).reverse();
    }
}

let weightGraph = new WeightedGraph();
weightGraph.addVertex("A");
weightGraph.addVertex("B");
weightGraph.addVertex("C");
weightGraph.addVertex("D");
weightGraph.addVertex("E");
weightGraph.addVertex("F");
weightGraph.addEdge("A", "B", 4);
weightGraph.addEdge("A", "C", 2);
weightGraph.addEdge("B", "E", 3);
weightGraph.addEdge("C", "D", 2);
weightGraph.addEdge("C", "F", 4);
weightGraph.addEdge("D", "E", 3);
weightGraph.addEdge("D", "F", 1);
weightGraph.addEdge("E", "F", 1);
// console.log(weightGraph.adjacencyList)
console.log(weightGraph.dijkstra("A", "E"))
// console.log(weightGraph);