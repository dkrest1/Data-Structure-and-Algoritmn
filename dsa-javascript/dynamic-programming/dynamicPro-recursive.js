//BIG O of the unperformant fib is O(2^N)

function fib(n) {
    if (n <= 2) return 1
    return fib(n - 1) + fib(n - 2);
}

// console.log("unperformant fib", fib(30));

//Memoization; to improve our solution of fibonacci numbers by storing those solution we solved already

function memoizationOfFib(n, memo = []) {
    if (memo[n] !== undefined) return memo[n];
    if (n <= 2) return 1;
    let res = memoizationOfFib(n - 1, memo) + memoizationOfFib(n - 2, memo);
    memo[n] = res;
    return res;
}
console.log("memoizationt fib", memoizationOfFib(100));

//another way to improve it is through tabular method
function tabularFib(n) {
    if (n <= 2) return 1;
    let fibNums = [0, 1, 1];
    for (let i = 3; i <= n; i++) {
        fibNums[i] = fibNums[i - 1] + fibNums[i - 2];
    }
    return fibNums[n];
}

console.log("tablular fib", tabularFib(100))