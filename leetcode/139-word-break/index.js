/*
    1st approach: recursion + memorization
    - e.g. "catsandogab", ["cats", "dog", "sand", "and", "cat", "og", "ab"]
        from the begining, we can split it into 2 strings
        [cat,sandogab], [cats, andogab]
        then they can become in the next recursion
        [cat,sand,ogab], [cat,sand,ogab]
        then 
        [cat,sand,og,ab], [cat,sand,og,ab]
    - actually we did [cat,sand,ogab], we know that "ogab" is breakable after the recursion,
        therefore we can save "ogab" as "true" so that we can avoid redundant computation if we meet "ogab" again

    Time    O(n^3)
    Space   O(n)

    84 ms, faster than 78.08%
*/
var wordBreak = function(s, wordDict) {
    const wordSet = new Set(wordDict)
    const cache = {}
    
    const dfs = idx => {
        if (idx == s.length) {
            return true
        }
        if (idx in cache) {
            return cache[idx]
        }
        let cur = ''
        for (let i = idx; i < s.length; i++) {
            cur += s[i]
            if (wordSet.has(cur)) {
                if (dfs(i+1)) {
                    return true
                }
            }
        }
        cache[idx] = false
        return false
    }

    return dfs(0)
};
