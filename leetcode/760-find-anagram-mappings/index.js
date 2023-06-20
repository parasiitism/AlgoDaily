/*
    1st: hashtable

	Time		O(N)
	Space		O(N)
	80 ms, faster than 48.43%
*/
var anagramMappings = function(A, B) {
    const n = nums1.length
    const ht = {}
    for (let i = 0; i < n; i++) {
        const x = nums2[i]
        if (x in ht === false) {
            ht[x] = []
        }
        ht[x].push(i)
    }

    const res = []
    for (let i = 0; i < n; i++) {
        const x = nums1[i]
        const arr = ht[x]
        const last = arr.pop()
        res.push(last)
    }
    
    return res
};