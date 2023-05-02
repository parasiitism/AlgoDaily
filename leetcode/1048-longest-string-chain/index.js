/*
    Hashtable
å
    - iterative bottom up with an DP array
    - iterate from the the shortest string to longest
        - slicing every character to see if there is a match in the dp array
        - if yes, use dp[key] + 1 to see if we can come up with the longest chain, save the 'longest' to avoid redundant calculation

    Time    O(NlogN + N*W*W)
    Space   O(N)
*/

/**
 * @param {string[]} words
 * @return {number}
 */
var longestStrChain = function(words) {
    words.sort((a, b) => a.length - b.length)
    const ht = {}
    for (let i = 0; i < words.length; i++) {
        const w = words[i]
        let longest = 0
        for (let j = 0; j < w.length; j++) {
            const key = w.slice(0, j) + w.slice(j+1)
            if (key in ht) {
                longest = Math.max(longest, ht[key])
            }
        }
        if (longest > 0) {
            ht[w] = longest + 1
        } else {
            ht[w] = 1
        }
    }
    return Math.max(...Object.values(ht))
};