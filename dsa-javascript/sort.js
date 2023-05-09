// bubble sort is a sorting algorithm whereby the largest value bubbles up
// 1st method
function bubbkeSort(arr) {
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

let result1 = bubbkeSort([1, 34, 56, 23, 56, 45])
console.log(result1)

// optimization of the above code
function optimizingBubbleSort(arr) {
    var noSwap;
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

let result2 = bubbkeSort([1, 34, 56, 23, 56, 45, 47, 78, 32, 36, 78])
console.log(result2)