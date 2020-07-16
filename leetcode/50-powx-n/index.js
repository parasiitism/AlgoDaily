/*
    3rd approach: dynamic programming
    - split the n (divide and conquer)

               2^10
            2^5 * 2^5
        2^2 * 2^3 * 2^2 * 2^3
    2^2 * 2^2 * 2 * 2^2 * 2^2 * 2

    Time    O(logn)
    Space   O(logn) recursion tree
    20 ms, faster than 96.88%
*/
var myPow = function (x, n) {
	if (n === 0) {
		return 1;
	}

	if (Math.abs(n) === 1) {
		return n > 0 ? x : 1 / x;
	}

	if (n % 2 === 0) {
		return myPow(x * x, n / 2);
	} else {
		return myPow(x * x, Math.floor(n / 2)) * x;
	}
};
