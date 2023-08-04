/*
    1st: top-down recursive
    - use a hashtable to avoid redundant calculation
	
    Time O(n)		duplicates are avoided so only the unseen numbers go through the calculations
	Space O(2n)	n for hashtable, n for recursive callstack
	72 ms, faster than 82.57%
*/
var climbStairs = function(n) {
    const cache = {}
    const f = i => {
        if (i < 0) {
            return 0
        }
        if (i == 0) {
            return 1
        }
        if (i in cache) {
            return cache[i]
        }
        cache[i] = f(i-1) + f(i-2)
        return cache[i]
    }
    return f(n)
}


/*
    2nd: bottom-up iterative

    dp[0] = 1
    dp[1] = 1
    dp[2] = 0 + 1 = 2
    dp[3] = 1 + 2 = 3
    dp[4] = 2 + 3 = 5
    dp[5] = 3 + 5 = 8
    dp[6] = 5 + 8 = 13

	Time 	O(n) iterate from 1 to N
	Space	O(n) for the array
	12ms beats 98.53%
*/
var climbStairs = function(n) {
    const dp = Array(n+1).fill(0)
    dp[1] = 1
    dp[2] = 2
    for (let i = 3; i <= n; i++) {
        dp[i] = dp[i-2] + dp[i-1]
    }
    return dp[n]
};

/*
    3rd: optimize the space

    Time 	O(n) iterate from 1 to N
	Space	O(1)
*/
var climbStairs = function(n) {
    if (n == 0) { return 0 }
    if (n == 1) { return 1 }
    let first = 1
    let second = 2
    for (let i = 3; i <= n; i++) {
        const c = first + second
        first = second
        second = c
    }
    return second
};