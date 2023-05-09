const { clearAllListeners } = require("@reduxjs/toolkit");

//1. linear search
function linearSearch(arr, target) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === target) return i
    }
    return -1
}

let result1 = linearSearch([1, 2, 3, 4, 5, 6], 6)
console.log(result1)

//binary search
function binarySearch(arr, target) {
    let start = 0;
    let end = arr.length - 1
    while (start <= end) {
        middle = Math.floor((start + end) / 2)
        if (arr[middle] === target) return middle
        else if (arr[middle] < target) {
            start = middle + 1
        } else {
            end = middle - 1
        }
    }
    return -1
}

let result2 = binarySearch([1, 2, 3, 4, 5, 6, 7, 10], 2)
console.log(result2)

//naive string
function naiveString(str, subArr) {
    let count = 0
    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < subArr.length; j++) {
            if (subArr[j] !== str[i + j]) {
                break;
            }
            if (j === subArr.length - 1) {
                count++
            }
        }
    }

    return count
}

let result3 = naiveString("hello the ello boy is", "pop")
console.log(result3)