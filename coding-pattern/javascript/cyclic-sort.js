
// //////////////////////////////////////////// Cyclic Sort (easy) //////////////////////
// Problem Statement #
// We are given an array containing ‘n’ objects. Each object, when created, was assigned a unique number from 1 to ‘n’ based on their creation sequence. This means that the object with sequence number ‘3’ was created just before the object with sequence number ‘4’.

// Write a function to sort the objects in-place on their creation sequence number in 
// �
// (
// �
// )
// O(n) and without any extra space. For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

// Example 1:

// Input: [3, 1, 5, 4, 2]
// Output: [1, 2, 3, 4, 5]
// Example 2:

// Input: [2, 6, 4, 3, 1, 5]
// Output: [1, 2, 3, 4, 5, 6]
// Example 3:

// Input: [1, 5, 6, 4, 3, 2]
// Output: [1, 2, 3, 4, 5, 6]


function cyclic_sort(arr) {
    let i = 0
    while (i < arr.length) {
        const j = arr[i] - 1

        if (arr[i] !== arr[j]) {
            [arr[i], arr[j]] = [arr[j], arr[i]]
        } else {
            i += 1
        }
    }
    return arr
}

const result1 = cyclic_sort([2, 6, 4, 3, 1, 5])


/////////////////////////////////// Find the Missing Number (easy) /////////////////////////////////////////

// Problem Statement #
// We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

// Example 1:

// Input: [4, 0, 3, 1]
// Output: 2
// Example 2:

// Input: [8, 3, 5, 2, 4, 6, 0, 1]
// Output: 7

function findMissingNumber(arr) {
    let i = 0
    n = arr.length


    while (i < n) {
        j = arr[i]

        if (arr[i] < n && arr[i] !== arr[j]) {
            [arr[i], arr[j]] = [arr[j], arr[i]]
        } else {
            i += 1
        }

    }

    for (let i = 0; i < n; i++) {
        if (arr[i] !== i) {
            return i
        }
    }

    return n
}

const result2 = findMissingNumber([8, 3, 5, 2, 4, 6, 0, 1])

function main() {
    console.log("result_one", result1)
    console.log("result_two", result2)
}

main()