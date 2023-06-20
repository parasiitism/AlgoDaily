/*
    1st approach:
    - since we need to find the min/max from a different array, we need 2 variables to store the previous min and max
    
    e.g.               min max
    [
        [4,5],
        [1,2,3],        4   5
        [1,2,2],        1   5
        [-10,1],        1   5
    ]

    144 ms, faster than 38.16%
*/
var maxDistance = function(arrays) {
    let res = 0
    let prevMin = arrays[0][0]
    let prevMax = arrays[0][arrays[0].length-1]
    for (let i = 1; i < arrays.length; i++) {
        const x = arrays[i]
        const mn = x[0]
        const mx = x[x.length-1]
        const a = Math.abs(mn - prevMax)
        const b = Math.abs(mx - prevMin)
        res = Math.max(res, a, b)

        prevMin = Math.min(prevMin, mn)
        prevMax = Math.max(prevMax, mx)
    }
    return res
};