function two_pointer(arr) {
    if(arr.length === 0) return 0

    let i = 0
    for(let j = 1; j < arr.length; j++) {
        if(arr[i] !== arr[j]) {
            i++
            arr[i] = arr[j]
        }
    }

    return i + 1
}

two_pointer([1,2,3,3,3,4,4,5,6,7, 9])