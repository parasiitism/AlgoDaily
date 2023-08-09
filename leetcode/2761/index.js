/*
    Eratosthenes + binary search

    Time    O(NlogN + PlogP)
    Space   O(N)
*/

/**
 * @param {number} n
 * @return {number[][]}
 */
var findPrimePairs = function(n) {
    const primes = genPrimes(n)
    const res = []
    for (let i = 0; i < primes.length; i++) {
        const x = primes[i]
        const partner = n - x
        const j = bsearch(primes, partner)
        if (j == -1) {
            continue
        }
        if (i > j) {
            break // break searching since we already explore the 2nd half 
        }
        res.push([x, primes[j]])
    }
    return res
};

const genPrimes = n => {
    const arePrimes = Array(n).fill(true)
    arePrimes[0] = false
    arePrimes[1] = false
    for (let i = 2; i*i < n; i++) {
        if (arePrimes[i] === false) {
            continue
        }
        for (let j = i*i; j < n; j+=i) {
            arePrimes[j] = false
        }
    }
    const primes = []
    for (let i = 0; i < n; i++) {
        if (arePrimes[i] === true) {
            primes.push(i)
        }
    }
    return primes
}

const bsearch = (A, target) => {
    let left = 0
    let right = A.length-1
    while (left <= right) {
        const mid = Math.floor((left + right) / 2)
        if (target < A[mid]) {
            right = mid - 1
        } else if (target > A[mid]) {
            left = mid + 1
        } else {
            return mid
        }
    }
    return -1
}