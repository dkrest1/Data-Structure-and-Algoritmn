// QUESTION : Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
// Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

///////////////////////////////////////////// BRUTE FORCE SOLUTION ///////////////////////////////////
function findAvg(arr, k) {
    let result = [];
    for (let i = 0; i < arr.length - k + 1; i++) {
        let sum = 0;
        for (let j = i; j < i + k; j++) {
            sum += arr[j]
        }
        result.push(sum / k)
    }

    return result;
}

// BIG O
//TIME COMPLEXITY O(N^2)
const result = findAvg([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
console.log("avgOfLengthOfArrBrute", result)

////////////////////////////////////////////////////// SLIDING WINDOW/////////////////////////////
function findAvgSlidingWindow(arr, k) {
    let result = [];
    let sum = 0,
        start = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
        if (i >= k - 1) {
            result.push(sum / k);
            sum -= arr[start];
            start += 1;
        }
    }
    return result;
}
//BIG O
//TIME COMPLEXITY O(N)
let result2 = findAvgSlidingWindow([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
console.log("avgOfLengthOfArrSliding =", result2)

///////////////////////////////////////// MAX SUB ARR IN AN ARRAY
// Question 2: Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
let arr2 = [2, 1, 5, 1, 3, 2]
let k2 = 3
//Explanation: Subarray with maximum sum is [5, 1, 3].

function maxSubArr(arr, k) {
    let maxSum = 0
    for (let i = 0; i < arr.length - k + 1; i++) {
        let sum = 0;
        for (let j = i; j < i + k; j++) {
            sum += arr[j];
            maxSum = Math.max(maxSum, sum);
        }
    }

    return maxSum;
}
// Time complexity O(n^2)
let result3 = maxSubArr(arr2, k2);
console.log("maxSubArrBrute =", result3)

function maxSubArrSlidindWindow(arr, k) {
    let maxSum = 0,
        start = 0,
        sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
        if (i >= k - 1) {
            maxSum = Math.max(maxSum, sum);
            sum -= arr[start];
            start += 1
        }
    }

    return maxSum
}
// Big O:
// Time Complexity: O(n)
// Space Complexity: O(1)
let result4 = maxSubArrSlidindWindow(arr2, k2)
console.log("maxSubArrSlidingWindow =", result4)


////////////////////////////////////////////////////// SMALLEST SUB ARRAY WITHIN A GIVEN SET /////////////////////////////////////////
// QUESTION 3.Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.
// Example 1:

// Input: [2, 1, 5, 2, 3, 2], S=7
//  Output: 2
//  Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
//  Example 2:

//  Input: [2, 1, 5, 2, 8], S=7
//  Output: 1
//  Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
//  Example 3:

//  Input: [3, 4, 1, 1, 6], S=8
//  Output: 3
//  Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
function findMinOfSubArr(arr, k) {
    let minLength = Infinity;
    let start = 0,
        sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i]
        while (sum >= k) {
            minLength = Math.min(minLength, i - start + 1)
            sum -= arr[start]
            start += 1
        }
    }

    if (minLength === Infinity) {
        return 0
    }

    return minLength
}

// Big O:
// Time Complexity: O(n)
// Space Complexity: O(1)

let result5 = findMinOfSubArr([3, 4, 1, 1, 6], 8)
console.log("minOfSubArr =", result5)


///////////////////////////////////////////////// Longest Substring with K Distinct Characters /////////////////////////////////////////
// Problem Statement #
// Given a string, find the length of the longest substring in it with no more than K distinct characters.

// Example 1:

// Input: String="araaci", K=2
// Output: 4
// Explanation: The longest substring with no more than '2' distinct characters is "araa".
// Example 2:

// Input: String="araaci", K=1
// Output: 2
// Explanation: The longest substring with no more than '1' distinct characters is "aa".
// Example 3:

// Input: String="cbbebi", K=3
// Output: 5
// Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi". 

function findLongestSubStringWithKChar(str, k) {
    let maxSubString = 0;
    let start = 0;
    let obj = {};
    for (let i = 0; i < str.length; i++) {
        let char = str[i];
        obj[char] = (obj[char] || 0) + 1
        console.log(obj)
        while (Object.keys(obj).length > k) {
            let char = str[start];
            obj[char] -= 1
            if (obj[char] === 0) delete obj[char]
            start += 1
        }
        maxSubString = Math.max(maxSubString, i - start + 1)
    }

    return maxSubString
}

let result6 = findLongestSubStringWithKChar("cbbebi", 3);
console.log("longgestSubStringWithDistinctChar", result6)