/*
    1st: hashtable
    - pre-comput a list of preferences for every person, which the list lists all the higher priority than his current partner 
    - for every person, loop over his perferences, if check if thier preference's perference has this person

    learned from others
    - https://www.youtube.com/watch?v=10laHayu2dc
    - https://leetcode.com/problems/count-unhappy-friends/solutions/844105/python-clean-solution/
*/
var unhappyFriends = function(n, preferences, pairs) {
    const d = {}
    for (let [u, v] of pairs) {
        const i = preferences[u].indexOf(v)
        const j = preferences[v].indexOf(u)
        d[u] = preferences[u].slice(0, i)
        d[v] = preferences[v].slice(0, j)
    }
    let res = 0
    for (let x in d) {
        for (let y of d[x]) {
            if (d[y].indexOf(parseInt(x)) !== -1) {
                res += 1
                break
            }
        }
    }
    return res
};

/*
    2nd: hashtable + hashset to optimize
*/
var unhappyFriends = function(n, preferences, pairs) {
    const priorities = {}
    for (let [u, v] of pairs) {
        const i = preferences[u].indexOf(v)
        const j = preferences[v].indexOf(u)
        priorities[u] = new Set(preferences[u].slice(0, i))
        priorities[v] = new Set(preferences[v].slice(0, j))
    }
    let res = 0
    for (let u = 0; u < n; u++) {
        for (let v of priorities[u]) {
            if (priorities[v].has(u)) {
                res += 1
                break
            }
        }
    }
    return res
};