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

//time complexity: O(n)

let result6 = findLongestSubStringWithKChar("cbbebi", 3);
console.log("longgestSubStringWithDistinctChar", result6)

// # ///////////////////////////////////////////// FRUITS INTO BASKET /////////////////////////////////////////////////////////////////////////////
// # PROBLEM STATEMENT
// # Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

// # You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

// # Write a function to return the maximum number of fruits in both the baskets.

// # Example 1:

// # Input: Fruit=['A', 'B', 'C', 'A', 'C']
// # Output: 3
// # Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
// # Example 2:

// # Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
// # Output: 5
// # Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
// # This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

function fruitInBasket(fruitArr) {
    let maxLength = 0;
    let start = 0;
    let fruitObj = {};
    for (let i = 0; i < fruitArr.length; i++) {
        let right_fruit = fruitArr[i]
        fruitObj[right_fruit] = (fruitObj[right_fruit] || 0) + 1
        while (Object.keys(fruitObj).length > 2) {
            let left_fruit = fruitArr[start]
            fruitObj[left_fruit] -= 1
            if (fruitObj[left_fruit] === 0) delete fruitObj[left_fruit]
            start += 1
        }

        maxLength = Math.max(maxLength, i - start + 1)
    }

    return maxLength
}

// time complexity: O(n)

let result7 = fruitInBasket(['A', 'B', 'C', 'A', 'C'])
console.log("fruitInBasket =", result7)

// # ////////////////////////////////////////////// NO REPEAT SUBSTRING //////////////////////////////////////////
// # Problem Statement #
// # Given a string, find the length of the longest substring which has no repeating characters.

// # Example 1:

// # Input: String="aabccbb"
// # Output: 3
// # Explanation: The longest substring without any repeating characters is "abc".
// # Example 2:

// # Input: String="abbbb"
// # Output: 2
// # Explanation: The longest substring without any repeating characters is "ab".
// # Example 3:

// # Input: String="abccde"
// # Output: 3
// # Explanation: Longest substrings without any repeating characters are "abc" & "cde".

function maxOfNoRepeatingStr(str) {
    let start = 0;
    let maxLength = 0;
    let obj = {};
    for (let i = 0; i < str.length; i++) {
        let char = str[i]
        if (char in obj) {
            start = Math.max(start, obj[char] + 1)
        }
        obj[char] = i
        maxLength = Math.max(maxLength, i - start + 1)
    }
    return maxLength
}
// time complexity = O(n)
let result8 = maxOfNoRepeatingStr("abbbb")
console.log("maxOfNoRepeatingString =", result8)

////////////////////////////////////////// Longest Substring with Same Letters after Replacement //////////////////////

// # Problem Statement #
// # Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

// # Example 1:

// # Input: String="aabccbb", k=2
// # Output: 5
// # Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
// # Example 2:

// # Input: String="abbcb", k=1
// # Output: 4
// # Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
// # Example 3:

// # Input: String="c", k=1
// # Output: 3
// # Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

function longestSubStringWithSameLetterAfterReplacement(str, k) {
    let start = 0;
    let maxRepeatedLetterCount = 0;
    let maxLength = 0;
    let obj = {};
    for (let i = 0; i < str.length; i++) {
        let rightStr = str[i]
        obj[rightStr] = (obj[rightStr] || 0) + 1
        maxRepeatedLetterCount = Math.max(maxRepeatedLetterCount, obj[rightStr])

        if (i - start + 1 - maxRepeatedLetterCount > k) {
            left_str = str[start]
            obj[left_str] - + 1
            start += 1
        }
        maxLength = Math.max(maxLength, i - start + 1)
    }

    return maxLength
}

// time complexity = O(n)
let result9 = longestSubStringWithSameLetterAfterReplacement("c", 1)
console.log("lonfestSubStringWithSameLetterAfterReplacement =", result9)

// # ///////////////////////////////////////// Longest Subarray with Ones after Replacement //////////////////////////
// #
// # Problem Statement #
// # Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

// # Example 1:

// # Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
// # Output: 6
// # Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
// # Example 2:

// # Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
// # Output: 9
// # Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.

function longestSubArrayWithOnesReplacement(arr, k) {
    let start = 0,
        maxLength = 0,
        maxOneCount = 0;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === 1) {
            maxOneCount += 1;
        }

        if ((i - start + 1 - maxOneCount) > k) {
            if (arr[start] === 1) {
                maxOneCount -= 1;
            }
            start += 1
        }
        maxLength = Math.max(maxLength, i - start + 1)
    }
    return maxLength
}

let result10 = longestSubArrayWithOnesReplacement(
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2)
console.log("longestSubStringWithSameLetterAfterReplacement =", result10)



