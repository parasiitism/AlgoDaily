/*
    1st approach: brute-force
    - try all the pairs to swap
    - find the max number
    - since the input is at most 1x10^8, there are at most 8*7 trials

    Time    O(logn x logn x logn)
    Space   O(logn) save the digit
    84 ms, faster than 20.53%
*/
var maximumSwap = function(num) {
    const nums = []
    const s = `${num}`
    for (let i = 0; i < s.length; i++) {
        nums.push(parseInt(s[i]))
    }
    let maxNum = num
    for (let i = 0; i < nums.length; i++) {
        for (let j = i+1; j < nums.length; j++) {
            // swap
            [nums[i], nums[j]] = [nums[j], nums[i]]
            const s = nums.join('')
            const temp = parseInt(s)
            if (temp > maxNum) {
                maxNum = temp
            }
            // swap back
            [nums[i], nums[j]] = [nums[j], nums[i]]
        } 
    }
    return maxNum
};

/*
    2nd:

    - Starting from the right, calculate the largest digit on the right of it. Example: for the number 4 3 1 8 3, we will can build the array: 8 8 8 8 3.
    - Now start from the left, the first digit that is smaller than the largest on its right is the one we want to swap.

    Time    O(N)
    Space   O(N)
*/
var maximumSwap = function(num) {
    const digits = [...`${num}`].map(c => Number(c))

    const n = digits.length
    const backward = Array(n).fill(n-1)
    let running_max_index = n-1
    for (let i = n-1; i >= 0; i--) {
        const x = digits[i]
        if (x > digits[running_max_index]) {
            running_max_index = i
        }
        backward[i] = running_max_index
    }
    for (let i = 0; i < n; i++) {
        const j = backward[i]
        if (digits[i] < digits[j]) {
            [digits[i], digits[j]] = [digits[j], digits[i]]
            return digits.map(x => `${x}`).join('')
        }
    }
    return num
};