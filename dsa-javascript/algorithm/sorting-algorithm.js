// bubble sort is a sorting algorithm whereby the largest value bubbles up
// 1st method
function bubbleSort(arr) {
    for (let i = arr.length; i > 0; i--) {
        for (let j = 0; j < i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                var temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            }
        }
    }

    return arr
}

let result1 = bubbleSort([1, 34, 56, 23, 56, 45])
console.log('result1 - ', result1)

// optimization of the above code
function optimizingBubbleSort(arr) {
    let noSwap;
    for (let i = arr.length; i > 0; i--) {
        noSwap = true
        for (let j = 0; j < i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                let temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                noSwap = false;
            }
        }
        if (noSwap) break
    }
    return arr
}
let result2 = optimizingBubbleSort([1, 34, 56, 23, 56, 45, 47, 78, 32, 36, 78])
console.log('result2 - ', result2)

////////////////////////// Selection  sort
// 1. optimized bubble sort
function selectionSort(arr) {
    for (let i = 0; i < arr.length; i++) {
        let lowest = i;
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[j] < arr[lowest]) {
                lowest = j
            }
        }

        if (i !== lowest) {
            let temp = arr[i]
            arr[i] = arr[lowest]
            arr[lowest] = temp
        }
    }
    return arr
}

let result3 = selectionSort([2, 3, 45, 64, 5, 7, 67, 89])
console.log('result3 - ', result3)

//////////////////////////// Insertion Sort
// function inserrtionSort(arr) {
//     for (let i = 1; i < arr.length; i++) {
//         let current = arr[i]
//         for (let j = i - 1; j >= 0 && arr[j] > current; j--) {
//             arr[j + 1] = arr[j]
//         }

//         arr[j + 1] = current;
//     }

//     return arr
// }
// let result4 = inserrtionSort([2, 3, 4, 5, 67, 8, 9, 0])
// console.log('result4 - ', result4)

//ps - implementation is not completed


////////////////////////////////////// MERGE SORT ////////////////////////////////

function merge(arr1, arr2) {
    let result = [];
    let i = 0;
    let j = 0;
    while (i < arr1.length && j < arr2.length) {
        if (arr1[i] < arr2[j]) {
            result.push(arr1[i])
            i++
        } else {
            result.push(arr2[j])
            j++
        }
    }

    while (i < arr1.length) {
        result.push(arr1[i])
        i++
    }

    while (j < arr2.length) {
        result.push(arr2[j])
        j++
    }
    return result;
}
let result5 = merge([1, 3, 4, 5, 7, 15, 34], [45, 47, 67])
console.log("result 5 - ", result5)

//continuation of mergesort as mergeSort uses recursion

function mergeSort(arr) {
    if (arr.length <= 1) return arr
    let mid = Math.floor(arr.length / 2)
    let left = mergeSort(arr.slice(0, mid))
    let right = mergeSort(arr.slice(mid))
    return merge(left, right)
}
let result6 = mergeSort([1, 5, 67, 34, 32, 456, 24, 56, 35, 567, 90])
console.log("resul6 - ", result6)

/////////////////////////Quick Sort
// 1st part pivot part
function pivot(arr, start = 0, end = arr.length - 1) {
    function swap(arr, i, j) {
        let temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    }

    let pivot = arr[start]
    let swapIndex = start
    for (let i = start + 1; i <= end; i++) {
        if (pivot > arr[i]) {
            swapIndex++
            swap(arr, swapIndex, i)
        }
    }

    swap(arr, start, swapIndex)
    return swapIndex
}

let result7 = pivot([4, 5, 44, 34, 23, 55, 2, 56, 99, 6, 26, 2, 55, 34])
console.log("result7 - ", result7)

// continuation of quick sort
function quickSort(arr, left = 0, right = arr.length) {
    if (left < right) {
        const pivotIndex = pivot(arr, left, end)
        //left
        quickSort(arr, left, pivotIndex - 1)
        //right
        quickSort(arr, pivotIndex + 1, right)
    }

    return arr
}

///////////////////Implementation of sorting algorithm
//helper function 1 to get a digit at a position in base 10
function getDigit(num, i) {
    return Math.floor(Math.abs(num) / Math.pow(10, i)) % 10
}
let result8 = getDigit(124566, 3)
console.log("result8 - ", result8)

//helpert function to get the length of a num
function digitCount(num) {
    if (num === 0) return 1;
    return Math.floor(Math.log10(Math.abs(num))) + 1
}
let result9 = digitCount(35433)
console.log("result9 - ", result9)

//helper function to get the highest length of num from an array
function getMostNumLength(arr) {
    let maxDigit = 0
    for (let i = 0; i < arr.length; i++) {
        maxDigit = Math.max(maxDigit, digitCount(arr[i]))
    }
    return maxDigit
}
let resul10 = getMostNumLength([123, 4566, 345, 567, 4455555, 33234444])
console.log("result10 - ", resul10)

//radix sort
function radixSort(nums) {
    let maxNum = getMostNumLength(nums)
    for (let k = 0; k < maxNum; k++) {
        let digitBucket = Array.from({ length: 10 }, () => [])
        for (let i = 0; i < nums.length; i++) {
            let digit = getDigit(nums[i], k)
            digitBucket[digit].push(nums[i])
        }

        nums = [].concat(...digitBucket)
    }
    return nums
}

let result11 = radixSort([12, 34, 22, 45, 11, 34])
console.log("result11 - ", result11)
