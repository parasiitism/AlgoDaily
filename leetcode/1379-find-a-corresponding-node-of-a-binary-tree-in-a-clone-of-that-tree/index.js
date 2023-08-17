/*
    1st: recursive DFS

    Time    O(N)
    Space   O(H)
    316 ms, faster than 76.83%
*/
var getTargetCopy = function(original, cloned, target) {
    if (original === null) {
        return null
    }
    if (original === target) {
        return cloned
    }
    const left = getTargetCopy(original.left, cloned.left, target)
    const right = getTargetCopy(original.right, cloned.right, target)
    return left ? left: right
};

/*
    2nd: BFS

    Time    O(N)
    Space   O(H)
    304 ms, faster than 93.42%
*/
var getTargetCopy = function(original, cloned, target) {
    const q = [[original, cloned]]
    while (q.length > 0) {
        const [a, b] = q.shift()
        if (a === target) {
            return b
        }
        if (a.left && b.left) {
            q.push([a.left, b.left])
        }
        if (a.right && b.right) {
            q.push([a.right, b.right])
        }
    }
    return null
};