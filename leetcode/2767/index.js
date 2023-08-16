/*
    recursion    

    Time    O(2^N)
    Spave   O(2^n)
*/
var minimumBeautifulSubstrings = function(s) {
    let res = 2**32
    const dfs = (idx, cnt) => {
        if (idx === s.length) {
            res = Math.min(res, cnt)
            return
        }
        let cur = ''
        for (let i=idx; i < s.length; i++) {
            if (cur.length == 0 && s[i] == '0') {
                break
            }
            cur += s[i]
            const x = parseInt(cur, 2)
            const exp = Math.floor(Math.log(x)/Math.log(5))
            if (5**exp === x) {
                dfs(i+1, cnt+1)
            }
        }
    }
    dfs(0, 0)
    if (res === 2**32) {
        return -1
    }
    return res
};