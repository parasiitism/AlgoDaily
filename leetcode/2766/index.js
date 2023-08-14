/*
    1st: hashtable

    Time    O(N + klogk)
    Space   O(N)
*/
var relocateMarbles = function(nums, moveFrom, moveTo) {
    const positions = new Set(nums) // {key : int}
    for (let i = 0; i < moveFrom.length; i++) {
        const from = moveFrom[i]
        const to = moveTo[i]
        if (!positions.has(from)) {
            continue
        }
        positions.delete(from)
        positions.add(to)
    }
    const res = Array.from(positions.keys())
    res.sort((a, b) => a - b)
    return res
};