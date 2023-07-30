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

    Time    O(W + N^3) the reason is string concat takes O(N)
    Space   O(N)

    84 ms, faster than 78.08%
*/
var wordBreak = function(s, wordDict) {
    const d = new Set(wordDict)
    const seen = new Set()
    
    const dfs = idx => {
        if (idx == s.length) {
            return true
        }
        if (seen.has(idx)) {
            return false
        }
        let cur = ''
        for (let i = idx; i < s.length; i++) {
            cur += s[i]
            if (d.has(cur)) {
                if (dfs(i+1) === true) {
                    return true
                }
            }
        }
        seen.add(idx)
        return false
    }

    return dfs(0)
};

/*
    DFS + wordDict iteration slicing

    Time    O(W+NWK)
    Space   O(W+N)
*/
var wordBreak = function(s, wordDict) {
    const d = new Set(wordDict)
    const seen = new Set()
    
    const dfs = i => {
        if (i == s.length) {
            return true
        }
        if (seen.has(i)) {
            return false
        }
        for (let w of d) {
            const n = w.length
            const sub = s.slice(i, i+n)
            if (w === sub) {
                if (dfs(i+n) === true) {
                    return true
                }
            }
        }
        seen.add(i)
        return false
    }

    return dfs(0)
};


/*
    3rd: BFS + string iteration

    Time    O(W+N^3)
    Space   O(W+N)
*/
var wordBreak = function(s, wordDict) {
    const d = new Set(wordDict)
    const seen = new Set()
    const q = [0]

    while (q.length > 0) {
        const i = q.shift()
        if (i == s.length) {
            return true
        }
        if (seen.has(i)) {
            continue
        }
        seen.add(i)
        let cur = ''
        for (let j = i; j < s.length; j++) {
            cur += s[j]
            if (d.has(cur)) {
                q.push(j+1)
            }
        }
    }
    return false
};

/*
    4th: BFS + wordDict iteration slicing

    Time    O(W+NWK)
    Space   O(W+N)
*/
var wordBreak = function(s, wordDict) {
    const d = new Set(wordDict)
    const seen = new Set()
    const q = [0]

    while (q.length > 0) {
        const i = q.shift()
        if (i == s.length) {
            return true
        }
        if (seen.has(i)) {
            continue
        }
        seen.add(i)
        for (let w of d) {
            const n = w.length
            const sub = s.slice(i, i+n)
            if (sub === w) {
                q.push(i+n)
            }
        }
    }
    return false
};