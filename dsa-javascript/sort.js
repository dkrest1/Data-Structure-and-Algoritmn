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

