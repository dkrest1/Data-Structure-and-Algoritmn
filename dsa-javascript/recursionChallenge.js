// example of recursive call
function recursionExponent(base, exponet) {
    if (exponet === 0) return 1
    return base * recursionExponent(base, exponet - 1)

}

let result1 = recursionExponent(2, 4)
console.log(result1)

function factorial(num) {
    if (num < 0) return 0
    if (num <= 1) return 1
    return num * factorial(num - 1)

}

let result2 = factorial(3)
console.log(result2)

function productOfArr(arr) {
    if (arr.length === 0) return 1
    return arr[0] * productOfArr(arr.slice(1))

}

let result3 = productOfArr([1, 2, 3, 4, 5])
console.log(result3)

function recursiveRange(num) {
    if (num === 0) return 0
    return num + recursiveRange(num - 1)

}
let result4 = recursiveRange(5)
console.log(result4)
















