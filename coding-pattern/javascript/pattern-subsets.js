const Deque = require("collections/deque")

////////////////////////////////// Subset Easy //////////////////////////////////////
// Problem Statement #
// Given a set with distinct elements, find all of its distinct subsets.

// Example 1:


// Input: [1, 3]
// Output: [], [1], [3], [1,3]
// Example 2:

// Input: [1, 5, 3]
// Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]

function find_subsets(nums) {
    const subsets = []
    
    subsets.push([])
    for(let i = 0; i < nums.length; i++) {
        let currentNum = nums[i]

        const n = subsets.length

        for(let j = 0; j < n; j++) {
            const set = subsets[j].slice(0)
            set.push(currentNum)
            subsets.push(set)
        }
    }

    return subsets
}

// Subsets With Duplicates (easy)


// Problem Statement #
// Given a set of numbers that might contain duplicates, find all of its distinct subsets.
// Example 1:

// Input: [1, 3, 3]
// Output: [], [1], [3], [1,3], [3,3], [1,3,3]
// Example 2:

// Input: [1, 5, 3, 3]
// Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3] 


function remove_duplicate_from_subset(nums) {
    nums.sort()
    const subsets = []
    subsets.push([])
    let startIndex = 0,
        endIndex = 0
    for(let i = 0; i < nums.length; i++) {
        startIndex = 0
        
        if(i > 0 && nums[i] === nums[i -1]) {
         startIndex = endIndex + 1
        }

        endIndex = subsets.length - 1
        for(j = startIndex; j < endIndex + 1; j++) {
            const set = subsets[j].slice(0)
            set.push(nums[i])
            subsets.push(set)
        }
    }

    return subsets
}

//////////////////////////////////////////// Permutations (medium) //////////////////////////////////////
// Problem Statement #
// Given a set of distinct numbers, find all of its permutations.

// Example 1:

// Input: [1,3,5]
// Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]

function find_permutation(nums) {
    const result = []
    // your code here
    let permutation = new Deque()
    permutation.push([])
    for(let i = 0; i < nums.length; i++) {
        const currentNum = nums[i]
        let n = permutation.length
        for(let p = 0; p < n; p++) {
            let oldPermutation = permutation.shift()

            for(let j= 0; j < oldPermutation.length + 1; j++) {
                const newPermutation = oldPermutation.slice(0)
                newPermutation.splice(j, 0, currentNum)
                if(newPermutation.length === nums.length) {
                    result.push(newPermutation)
                }else {
                    permutation.push(newPermutation)
                }
            }
        }
    }
    return result
}

function main() {
    // const result1 = find_subsets([1, 5, 3])
    // result1.forEach(subset => console.log(subset))

    // const result2 = remove_duplicate_from_subset([1,5, 3, 3])
    // result2.forEach(subset => console.log(subset))

    const result3 = find_permutation([1, 3, 5])
    console.log(result3)

}

main()