/*
    Given an array of monthly profit, return the number of continuous k-months that the profits are increasing
    
    e.g.
    A = [5, 3, 5, 7, 8, 3], k = 3
            -------
               -------
    The result = 2, because [3,5,7] and [5,7,8] are increasing subarrays
*/
const f = (A, k) => {
    const n = A.length
    let j = 0
    let res = 0
    for (let i = 1; i < n; i++) {
        if (A[i] > A[i-1]) {
            if (i-j+1 > k) {
                j += 1
            }
            if (i-j+1 == k) {
                res += 1
            }
        } else {
            j = i
        }
    }
    return res
}

console.log(f([5,3,5,7,8,1], 3))
console.log(f([5,3,5,7,8], 3))
console.log(f([5,3,5,7,8,9], 3))
console.log(f([5,3,5,7,1], 3))

console.log(f([1,2,3,4,5,1], 5))
console.log(f([1,2,3,4,5,1], 4))
console.log(f([1,2,3,4,5,1], 3))
console.log(f([1,2,3,4,5,1], 2))