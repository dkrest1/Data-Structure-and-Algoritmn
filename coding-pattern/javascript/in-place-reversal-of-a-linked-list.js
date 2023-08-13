// ////////////////////// Reverse a LinkedList (easy) ////////////////////////
// Problem Statement #
// Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the reversed LinkedList.

class Node {
    constructor(value, next = null) {
        this.value = value
        this.next = next
    }

    print_list() {
        let temp = this
        while (temp !== null) {
            process.stdout.write(`${temp.value} `)
            temp = temp.next
        }
        console.log()
    }

}

function reverseLinkedList(head) {
    let current = head
    let previous = null
    while (current !== null) {
        next = current.next
        current.next = previous
        previous = current
        current = next
    }

    return previous
}

// ///////////////////////////////////////// / Reverse a Sub-list (medium)////////////////
// Problem Statement #
// Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.

function reverseSubList(head, node1, node2) {
    if (node1 === node2) {
        return head
    }

    let previous = null
    let current = head
    let i = 0
    while (current !== null && i < node1 - 1) {
        previous = current
        current = current.next
        i += 1
    }

    i = 0
    let last_node_of_the_first_part = previous
    let last_node_of_the_sub_list = current
    let next = null


    while (current !== null && i < node2 - node1 + 1) {
        next = current.next
        current.next = previous
        previous = current
        current = next
        i += 1
    }

    if (last_node_of_the_first_part !== null) {
        last_node_of_the_first_part.next = previous
    } else {
        previous = head
    }

    last_node_of_the_sub_list.next = current
    return head

}

// Reverse every K-element Sub-list (medium)

function reverse_every_k_element(head, k) {
    if (k <= 1 || head === null) {
        return head
    }

    let previous = null
    let current = head

    while (true) {
        const last_node_of_the_previous_list = previous;
        const last_node_of_the_sub_list = current
        let next = null

        let i = 0

        while (current !== null && i < k) {
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1
        }

        if (last_node_of_the_previous_list !== null) {
            last_node_of_the_previous_list.next = previous
        } else {
            head = previous
        }

        last_node_of_the_sub_list.next = current

        if (current !== null) {
            break
        }

        previous = last_node_of_the_sub_list
    }

    return head

}


function main() {
    const head = new Node(1)
    head.next = new Node(2)
    head.next.next = new Node(3)
    head.next.next.next = new Node(4)
    head.next.next.next.next = new Node(5)
    head.next.next.next.next.next = new Node(6)
    head.next.next.next.next.next.next = new Node(7)
    head.next.next.next.next.next.next.next = new Node(8)

    process.stdout.write("Node of the original LinkedList are: ")
    head.print_list()
    let result = reverse_every_k_element(head, 3)
    process.stdout.write("Node of the reversed LinkedList are: ")
    result.print_list()


}

main()