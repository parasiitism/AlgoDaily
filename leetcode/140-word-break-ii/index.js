/*
    classic approach: bottom-up recursion + memorization
    - similar to lc131, 132, 139, 140
    - see ./idea.png

    ref:
    - https://leetcode.com/problems/word-break-ii/discuss/44167/My-concise-JAVA-solution-based-on-memorized-DFS

    Time    O(n^2*k) Size of recursion tree can go up to n^2. The creation of list takes k time.
    Space   O(n^2*k)
    76 ms, faster than 96.35%
*/
var wordBreak = function(s, wordDict) {
    const wordSet = new Set(wordDict)
    const cache = {}
    
    const dfs = idx => {
        if (idx === s.length) {
            return [[]]
        }
        if (idx in cache) {
            return cache[idx]
        }
        const subResult = []
        let cur = ''
        for (let i = idx; i < s.length; i++) {
            cur += s[i]
            if (wordSet.has(cur)) {
                const sentences = dfs(i+1)
                for (let words of sentences) {
                    const _words = [cur, ...words]
                    subResult.push(_words)
                }
            }
        }
        cache[idx] = subResult
        return subResult
    }
    const sentenses = dfs(0)
    return sentenses.map(v => v.join(" "))
};

/*
    2nd: just recursion
    - we don't need DP for this question
    - the reason we have to print all the possibilities - meaning that we have to append subresults for every match anyway, so DP doesn't help 
*/
var wordBreak = function(s, wordDict) {
    const wordSet = new Set(wordDict)
    const dfs = idx => {
        if (idx === s.length) {
            return [[]]
        }
        const subResult = []
        let cur = ''
        for (let i = idx; i < s.length; i++) {
            cur += s[i]
            if (wordSet.has(cur)) {
                const sentences = dfs(i+1)
                for (let words of sentences) {
                    const _words = [cur, ...words]
                    subResult.push(_words)
                }
            }
        }
        return subResult
    }
    const sentenses = dfs(0)
    return sentenses.map(v => v.join(" "))
};
/*
    same as above
*/
var wordBreak = function(s, wordDict) {
    const wordSet = new Set(wordDict)
    const res = []
    
    const dfs = (idx, path) => {
        if (idx === s.length) {
            return res.push(path)
        }
        let cur = ''
        for (let i = idx; i < s.length; i++) {
            cur += s[i]
            if (wordSet.has(cur)) {
                dfs(i+1, [...path, cur])
            }
        }
    }
    dfs(0, [])
    return res.map(v => v.join(" "))
};
/*
    same as above + wordDict iteration
*/
var wordBreak = function(s, wordDict) {
    const d = new Set(wordDict)
    const res = []
    const dfs = (idx, path) => {
        if (idx == s.length) {
            return res.push(path)
        }
        for (let w of d) {
            const n = w.length
            const sub = s.slice(idx, idx+n)
            if (sub === w) {
                const _path = [...path, w]
                dfs(idx+n, _path)
            }
        }
    }
    dfs(0, [])
    return res.map(arr => arr.join(' '))
};