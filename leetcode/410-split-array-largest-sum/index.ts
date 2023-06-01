/*
    1st: dynamic programming, recursion + hashtable
    - similar to lc813, 1043, 1335

    Time    O(M * N^3)
    Space   O(NM)

    LTE 
    29 / 31 test cases passed.
*/
function splitArray(nums: number[], k: number): number {
    return dfs(nums, k, {})
};

const dfs = (nums: number[], k: number, cache: Object): number => {
    if (k == 1) {
        return sum(nums)
    }
    const key = `${nums.length},${k}`
    if (key in cache) {
        return cache[key]
    }
    let curSum = 0
    let smallestMax = 2**32
    for (let i = 0; i < nums.length; i++) {
        curSum += nums[i]
        const sub = nums.slice(i+1)
        const nextSum = dfs(sub, k - 1, cache)
        const largest = Math.max(curSum, nextSum)
        smallestMax = Math.min(smallestMax, largest)
    }
    cache[key] = smallestMax
    return smallestMax
}

const sum = (A: number[]): number => {
    return A.reduce((agg, a) => agg+a, 0)
}

/*
    2nd: 
    - optimization 1: using an index to indicate the start instead of doing array slicing

    Time    O(M * N^2)
    Space   O(MN)
    6763 ms beats 8.33%
*/
function splitArray(nums: number[], k: number): number {
    return dfs(nums, 0, k, {})
};

const dfs = (nums: number[], start: number, k: number, cache: Object): number => {
    if (k == 1) {
        return sum(nums, start)
    }
    const key = `${start},${k}`
    if (key in cache) {
        return cache[key]
    }
    let curSum = 0
    let smallestMax = 2**32
    for (let i = start; i < nums.length; i++) {
        curSum += nums[i]
        const nextSum = dfs(nums, i+1, k-1, cache)
        const largest = Math.max(curSum, nextSum)
        smallestMax = Math.min(smallestMax, largest)
    }
    cache[key] = smallestMax
    return smallestMax
}

const sum = (A: number[], from: number): number => {
    let total = 0
    for (let i = from; i < A.length; i++) {
        total += A[i]
    }
    return total
}

/*
    3rd: 
    - optimization 2: use a suffix array to avoid redundant summation

    Time    O(M * N^2)
    Space   O(MN)
    6517 ms beats 5.64%
*/
function splitArray (nums: number[], k: number): number {
    const n = nums.length
    const suffixSums = Array(n).fill(0)
    let sfs = 0
    for (let i = n-1; i >= 0; i--) {
        sfs += nums[i]
        suffixSums[i] = sfs
    }
    console.log(suffixSums)
    return dfs(nums, 0, k, {}, suffixSums)
};

const dfs = (nums: number[], start: number, k: number, cache: Object, suffixSums: number[]): number => {
    if (k == 1) {
        return suffixSums[start]
    }
    const key = `${start},${k}`
    if (key in cache) {
        return cache[key]
    }
    let curSum = 0
    let smallestMax = 2**32
    for (let i = start; i < nums.length-1; i++) {
        curSum += nums[i]
        const nextSum = dfs(nums, i+1, k-1, cache, suffixSums)
        const largest = Math.max(curSum, nextSum)
        smallestMax = Math.min(smallestMax, largest)
        // console.log(curSum, nextSum)
    }
    cache[key] = smallestMax
    return smallestMax
}