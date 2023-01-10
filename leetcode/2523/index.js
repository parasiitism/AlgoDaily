/*
    1st: brute force + binary search
    - generate all the primes from 2 to right
    - binary search the left-most prime >= left and iterate thru the primes and get the result
    
    Time    O(right)
    Space   O(primes)
    Runtime 674 ms Beats 100%
*/
var closestPrimes = function(left, right) {
    let primes = getPrimes(right + 1)
    const idx = lowerBsearch(primes, left)
    let res = [-1,-1]
    let min_diff = 2**32
    for (let i = idx + 1; i < primes.length; i++) {
        let diff = primes[i] - primes[i-1]
        if (diff < min_diff) {
            min_diff = diff
            res = [primes[i-1], primes[i]]
        }
    }
    return res
};

var getPrimes = function(n) {
    const arePrimes = Array(n).fill(true)
    arePrimes[0] = false
    arePrimes[1] = false
    for (let i = 2; i*i <= n; i++) {
        if (arePrimes[i] === false) {
            continue
        }
        for (let j = i; i*j <= n; j++) {
            arePrimes[i*j] = false
        }
    }
    const primes = []
    for (let i = 0; i < arePrimes.length; i++) {
        if (arePrimes[i] === true) {
            primes.push(i)
        }
    }
    return primes
};

const lowerBsearch = (nums, target) => {
	let left = 0;
	let right = nums.length;
	while (left < right) {
		const mid = Math.floor((left + right) / 2);
		if (target <= nums[mid]) {
			right = mid;
		} else {
			left = mid + 1;
		}
	}
	return left;
};