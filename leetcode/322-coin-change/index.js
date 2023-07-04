/*
    1st approach: top-down dfs + hashtable

    Time    O(CA) C: number of coins, A: amount
    Space   O(A)
    168 ms, faster than 27.24%
*/
var coinChange = function(coins, amount) {
    const cache = {}
    const dfs = remain => {
        if (remain < 0) {
            return 2**32
        }
        if (remain == 0) {
            return 0
        }
        if (remain in cache) {
            return cache[remain]
        }
        let minCnt = 2**32
        for (let c of coins) {
            const cnt = dfs(remain - c) + 1
            minCnt = Math.min(minCnt, cnt)
        }
        cache[remain] = minCnt
        return minCnt
    }
    const res = dfs(amount)
    if (res === 2**32) { return -1 }
    return res
};

/*
    2nd: dp
    learned from others: bottom-up
    e.g. coins = [1,2,5], amount = 7
    f(0) = 0  so if f(100-100), it output 0+1=1
    f(1) = min(f(0)) + 1
    f(2) = min(f(1)+f(0)) + 1
    f(3) = min(f(2)+f(1)) + 1
    f(4) = min(f(3)+f(2)) + 1
    f(5) = min(f(4)+f(3)+f(0)) + 1
    f(6) = min(f(5)+f(4)+f(1)) + 1
    f(7) = min(f(6)+f(5)+f(2)) + 1
    ...

    Time    O(CA) C: number of coins, A: amount
    Space   O(A)
    152 ms, faster than 42.49%
*/
var coinChange = function (coins, amount) {
	const dp = Array(amount+1).fill(2**32)
    dp[0] = 0
    for (let i = 1; i <= amount; i++) {
        for (let c of coins) {
            if (i - c >= 0) {
                dp[i] = Math.min(dp[i], dp[i-c]+1)
            }
        }
    }
    if (dp[amount] === 2**32) {
        return -1
    }
    return dp[amount]
};
