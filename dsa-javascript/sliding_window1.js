function maxSubArr(arr, num) {
    if(arr.length < num) {
        return null
    }

    let tempSum = 0
    let maxSum = 0
    for(let i = 0; i < num; i++) {
        maxSum += arr[i]
    }
    tempSum = maxSum
    for(let i = num; i < arr.length; i++) {
        tempSum = tempSum + arr[i] - arr[i - num]
        maxSum = Math.max(maxSum, tempSum)
    }
    
    return maxSum
}

maxSubArr([1,2,3,4,5,6,6], 3)