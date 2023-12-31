/*
    Input:
    A = [22, 19, 18, 15, 14, 10, 5, 1, 3, 4, 7, 20, 25]
    k = 21

    Output: the number of elements in A strictly greater than k. In this case, output will be 2.

---- Questions to ask ----
    - will there will any duplicate numbers?
*/

const largerThanX = (A, k) => {
    const n = A.length
    // binary search the dip
    const dipIdx = findDip(A)
    if (A[dipIdx] > k) {
        return n
    }
    // do binary search on the left
    const left = bSearchLeft(A, k, dipIdx)
    // do binary search on the right
    const right = bSearchRight(A, k, dipIdx)
    console.log(left, dipIdx, right)
    return (left + 1) + (n - right)
}

// upper bound
const findDip = A => {
    let left = 0
    let right = A.length-1
    while (left < right) {
        const mid = Math.floor((left + right)/2)
        if (A[mid] < A[mid+1]) {
            right = mid
        } else {
            left = mid + 1
        }
    }
    return left
}

const bSearchLeft = (A, target, dipIdx) => {
    let left = -1
    let right = dipIdx - 1
    while (left < right) {
        const mid = Math.ceil((left + right) / 2)
        if (target < A[mid]) {
            left = mid
        } else {
            right = mid - 1
        }
    }
    return left
}

// upper bound
const bSearchRight = (A, target, dipIdx) => {
    let left = dipIdx + 1
    let right = A.length
    while (left < right) {
        const mid = Math.floor((left + right) / 2)
        if (target < A[mid]) {
            right = mid
        } else {
            left = mid + 1
        }
    }
    return left
}

let a = [22, 19, 18, 15, 14, 10, 5, 1, 3, 4, 7, 20, 25]
let b = 21
console.log(largerThanX(a, b)) // (0, 7, 12), 2

a = [23, 22, 19, 18, 15, 14, 10, 5, 1, 3, 4, 7, 20, 25]
b = 21
console.log(largerThanX(a, b)) // (1, 8, 13), 13

a = [19, 18, 15, 14, 10, 5, 1, 3, 4, 7, 20, 25]
b = 21
console.log(largerThanX(a, b)) // (-1, 6, 11), 1

a = [22, 19, 18, 15, 14, 10, 5, 1, 3, 4, 7, 20, 25]
b = 0
console.log(largerThanX(a, b)) // 13

a = [22, 19, 18, 15, 14, 10, 5, 1, 3, 4, 7, 20, 25]
b = 1
console.log(largerThanX(a, b)) // (6, 7, 8), 12

a = [1, 3, 4, 7, 20, 25]
b = 1
console.log(largerThanX(a, b)) // (-1, 0, 1), 5

a = [1, 3, 4, 7, 20, 25]
b = 0
console.log(largerThanX(a, b)) // 6

a = [22, 19, 18, 15, 14, 10, 5, 1]
b = 1
console.log(largerThanX(a, b)) // (6, 7, 8), 7

a = [22, 19, 18, 15, 14, 10, 5, 1]
b = 0
console.log(largerThanX(a, b)) // 8