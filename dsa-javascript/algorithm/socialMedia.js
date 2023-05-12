// {DIVIDE AND CONQUER ALGORITHM}

// linear search algorithm
function linear(arr, target) {
    for (let i = 0; i < arr.length; i++) {
        arr[i] === target ? i : -1
    }
}

//binary search
function binarySearch(arr, target) {
    let min = 0;
    let max = arr.length - 1;
    while (min <= max) {
        let middle = Math.floor((min + max) / 2)
        if (arr[middle] === target) {
            return middle
        } else if (arr[middle] < target) {
            min = middle + 1;
        } else {
            max = middle - 1;
        }
    }

    return null;
}

console.log(binarySearch([1, 2, 3, 4, 5], 1))