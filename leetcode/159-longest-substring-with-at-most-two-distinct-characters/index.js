/*
    1st: 2pointers + hashtable
    - similar to lc3, 340, 904
    - maintain the sliding window to have 2 unique keys

    Time    O(N)
    Space   O(N)
    148 ms, faster than 15.16%
*/
var lengthOfLongestSubstringTwoDistinct = function (s) {
	const counter = {}
    let res = 0
    let j = 0
    for (let i = 0 ; i < s.length; i++) {
        const c = s[i]
        if (c in counter === false) {
            counter[c] = 0
        }
        counter[c] += 1
        
        while (Object.keys(counter).length > 2) {
            const left = s[j]
            j += 1
            counter[left] -= 1
            if (counter[left] === 0) {
                delete counter[left]
            }
        }
        res = Math.max(res, i - j + 1)
    }
    return res
};
