/*
    1st: sort the end times
    - activity selection
    - similar to lc56, 252, 253, 435, 452, 646

    ref:
    - https://www.cse.cuhk.edu.hk/~taoyf/course/3160/19-fall/lec/disj_intv.pdf
    - https://en.wikipedia.org/wiki/Activity_selection_problem

    Time    O(NlogN)
    Space   O(N)
    88 ms, faster than 93.02%
*/
var findLongestChain = function (pairs) {
	pairs.sort((a, b) => a[1] - b[1])
    let max_end = -(2**32)
    let res = 0
    for (let [s, e] of pairs) {
        if (s > max_end) {
            max_end = e
            res += 1
        }
    }
    return res
};
