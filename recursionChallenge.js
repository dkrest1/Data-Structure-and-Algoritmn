// example of recursive call
//1. finding the power 
function recursionExponent(base, exponet) {
    if (exponet === 0) return 1
    return base * recursionExponent(base, exponet - 1)

}
let result1 = recursionExponent(2, 4)
console.log(result1)

// 2. factorial
function factorial(num) {
    if (num < 0) return 0
    if (num <= 1) return 1
    return num * factorial(num - 1)

}
let result2 = factorial(3)
console.log(result2)

//3. product of an array
function productOfArr(arr) {
    if (arr.length === 0) return 1
    return arr[0] * productOfArr(arr.slice(1))

}
let result3 = productOfArr([1, 2, 3, 4, 5])
console.log(result3)

//4. add the nums 
function recursiveRange(num) {
    if (num === 0) return 0
    return num + recursiveRange(num - 1)

}
let result4 = recursiveRange(5)
console.log(result4)

//5. reverse string
function reverseString(str) {
    if (str.length <= 1) return str

    return reverseString(str.slice(1)) + str[0]
}
let result5 = reverseString("hello")
console.log(result5)

//6. isPalindrome 
function isPalindrome(str) {
    if (str.length === 1) return true
    if (str.length === 2) return str[0] === str[1]
    if (str[0] === str.slice(-1)) return isPalindrome(str.slice(1, -1))
    return false
}
let result6 = isPalindrome("aabbaa")
console.log(result6)

//7. flatten an array 
function flattenAr(arr) {
    let newArr = [];
    for (let i = 0; i < arr.length; i++) {
        if (Array.isArray(arr[i])) {
            newArr = newArr.concat(flattenAr(arr[i]))
        } else {
            newArr.push(arr[i])
        }
    }
    return newArr
}
let result7 = flattenAr([1, 2, ["a", ["b", ["c"]]], 3, ["d", ["e", ["f"]]]])
console.log(result7)

//8. fibonacci sequence
//FIBONACCI SOLUTION
function fib(n) {
    if (n <= 2) return 1;
    return fib(n - 1) + fib(n - 2);
}
let result8 = fib(6)
console.log(result8)

//9. capitalize words of an array
function capitalizeWords(arr) {
    if (arr.length === 1) return [arr[0].toUpperCase()]
    let res = capitalizeWords(arr.slice(0, -1))
    res.push(arr.slice(arr.length - 1)[0].toUpperCase())
    return res

}
let result9 = capitalizeWords(["hello", "tosin", "omolola"])
console.log(result9)


//////////////////////////////////////////////////////////////////////////////////

// nestedEvenSum Solution

function nestedEvenSum(obj, sum = 0) {
    for (var key in obj) {
        if (typeof obj[key] === 'object') {
            sum += nestedEvenSum(obj[key]);
        } else if (typeof obj[key] === 'number' && obj[key] % 2 === 0) {
            sum += obj[key];
        }
    }
    return sum;
}
//capitalizeFire Solution

function capitalizeFirst(array) {
    if (array.length === 1) {
        return [array[0][0].toUpperCase() + array[0].substr(1)];
    }
    const res = capitalizeFirst(array.slice(0, -1));
    const string = array.slice(array.length - 1)[0][0].toUpperCase() + array.slice(array.length - 1)[0].substr(1);
    res.push(string);
    return res;
}
//stringifyNumbers Solution

function stringifyNumbers(obj) {
    var newObj = {};
    for (var key in obj) {
        if (typeof obj[key] === 'number') {
            newObj[key] = obj[key].toString();
        } else if (typeof obj[key] === 'object' && !Array.isArray(obj[key])) {
            newObj[key] = stringifyNumbers(obj[key]);
        } else {
            newObj[key] = obj[key];
        }
    }
    return newObj;
}
//collectStrings Solution: Helper Method Recursion Version

function collectStrings(obj) {
    var stringsArr = [];

    function gatherStrings(o) {
        for (var key in o) {
            if (typeof o[key] === 'string') {
                stringsArr.push(o[key]);
            }
            else if (typeof o[key] === 'object') {
                return gatherStrings(o[key]);
            }
        }
    }

    gatherStrings(obj);

    return stringsArr;
}
//collectStrings Solution: Pure Recursion Version

function collectStrings(obj) {
    var stringsArr = [];
    for (var key in obj) {
        if (typeof obj[key] === 'string') {
            stringsArr.push(obj[key]);
        }
        else if (typeof obj[key] === 'object') {
            stringsArr = stringsArr.concat(collectStrings(obj[key]));
        }
    }

    return stringsArr;
}


