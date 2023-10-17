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

function main() {
    const result1 = find_subsets([1, 5, 3])
    result1.forEach(subset => console.log(subset))
}

main()