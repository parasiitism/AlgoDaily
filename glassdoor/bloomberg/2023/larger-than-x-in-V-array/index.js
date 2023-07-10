/*
    Input:
    A = [22, 19, 18, 15, 14, 10, 5, 1, 3, 4, 7, 20, 25]
    k = 21

    Output: the number of elements in A strictly greater than k. In this case, output will be 2.

---- Questions to ask ----
    - will there will any duplicate numbers?
*/

const largerThanX = (A, k) => {
    // binary search the dip
    const dipIdx = findDip(A)
    // do binary search on the left
    const left = bSearchLeft(A, k, dipIdx-1)
    // do binary search on the right
    const right = bSearchRight(A, k, dipIdx)
    console.log(dipIdx, left, right)
    return left + A.length - right + 1
}

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
    let left = 0
    let right = dipIdx
    let res = -1
    while (left <= right) {
        const mid = Math.floor((left + right) / 2)
        if (target >= A[mid]) {
            right = mid - 1
        } else {
            res = mid
            left = mid + 1
        }
    }
    return res
}

const bSearchRight = (A, target, dipIdx) => {
    let left = dipIdx
    let right = A.length - 1
    let res = A.length
    while (left <= right) {
        const mid = Math.floor((left + right) / 2)
        if (target >= A[mid]) {
            left = mid + 1
        } else {
            res = mid
            right = mid - 1
        }
    }
    return res
}

let a = [22, 19, 18, 15, 14, 10, 5, 1, 3, 4, 7, 20, 25]
let b = 21
console.log(largerThanX(a, b))

a = [23, 22, 19, 18, 15, 14, 10, 5, 1, 3, 4, 7, 20, 25]
b = 21
console.log(largerThanX(a, b))

a = [19, 18, 15, 14, 10, 5, 1, 3, 4, 7, 20, 25]
b = 21
console.log(largerThanX(a, b))

a = [22, 19, 18, 15, 14, 10, 5, 1, 3, 4, 7, 20, 25]
b = 0
console.log(largerThanX(a, b))

a = [22, 19, 18, 15, 14, 10, 5, 1, 3, 4, 7, 20, 25]
b = 1
console.log(largerThanX(a, b))

a = [1, 3, 4, 7, 20, 25]
b = 1
console.log(largerThanX(a, b))

a = [1, 3, 4, 7, 20, 25]
b = 0
console.log(largerThanX(a, b))

a = [22, 19, 18, 15, 14, 10, 5, 1]
b = 1
console.log(largerThanX(a, b))

a = [22, 19, 18, 15, 14, 10, 5, 1]
b = 0
console.log(largerThanX(a, b))