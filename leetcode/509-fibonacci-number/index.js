/*
    1st: top-down recursive
	- use a hashtable to avoid redundant calculation
	
    Time O(n)		duplicates are avoided so only the unseen numbers go through the calculations
	Space O(2n)	    n for hashtable, n for recursive callstack
	68 ms, faster than 79.80% 
*/
var fib = function(n) {
    const cache = {}
    const f = i => {
        if (i == 0) {
            return 0
        }
        if (i == 1) {
            return 1
        }
        if (i in cache) {
            return cache[i]
        }
        cache[i] = f(i-1) + f(i-2)
        return cache[i]
    }
    return f(n)
};

/*
    2nd: bottom-up iterative

	Time 	O(n) iterate from 1 to N
	Space	O(n) for the array
	76 ms, faster than 70.93%
*/
var fib = function (N) {
	const dp = [0, 1];
	for (let i = 2; i <= N; i++) {
		dp.push(dp[i - 2] + dp[i - 1]);
	}
	return dp[N];
};

/*
    3rd: bottom-up iterative

	Time 	O(n) iterate from 1 to N
	Space	O(1) for the array
*/
var fib = function(n) {
    if (n == 0) { return 0 }
    if (n == 1) { return 1 }
    let first = 0
    let second = 1
    for (let i = 2; i <= n; i++) {
        const c = first + second
        first = second
        second = c
    }
    return second
};