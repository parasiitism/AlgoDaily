/*
    3rd: 2d array DP

    ref: 
    - https://www.youtube.com/watch?v=DJ4a7cmjZY0
    - https://www.youtube.com/watch?v=jaNZ83Q3QGc
    - https://leetcode.com/problems/coin-change-2/discuss/674977/100-Faster-or-Recursive-1-d-2-d-DP-or-Matrix-With-Example-or-Commented
*/
var change = function (amount, coins) {
	if (amount == 0) {
		return 1;
	}
	const ways = Array(amount + 1).fill(0);
	ways[0] = 1;
	for (let c of coins) {
		for (let j = 1; j <= amount; j++) {
			const remain = j - c;
			if (j - c >= 0) {
				ways[j] += ways[j - c];
			}
		}
	}
	return ways[amount];
};

/*
    This is very similar to lc377, the only difference is
    - lc377 cares about the order
    - this question doesn't care

    So we use (index, remain) to cache the number of combinations of every sub-problem 
*/
var change = function(amount, coins) {
    const cache = {}
    const dfs = (start, remain) => {
        if (remain < 0) {
            return 0
        }
        if (remain == 0) {
            return 1
        }
        const key = `${start},${remain}`
        if (key in cache) {
            return cache[key]
        }
        let total = 0
        for (let i = start; i < coins.length; i++) {
            const c = coins[i]
            total += dfs(i, remain - c)
        }
        cache[key] = total
        return total
    }
    return dfs(0, amount)
};