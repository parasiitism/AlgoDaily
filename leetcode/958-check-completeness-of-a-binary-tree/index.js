/*
    2nd approach: level order traversal
	- on a level, there are 2 possible reasons which make the binary tree not complete
		1. there is a null on my left(given that i am a non-null node)
		2. there is a null above my level(given that i am a non-null node)

	Time	O(n)
	Space	O(n)
	88 ms, faster than 65.91%
*/
var isCompleteTree = function(root) {
    const q = [root]
    let seenNullAbove = false
    while (q.length > 0) {
        const n = q.length
        let seenNull = false
        for (let i = 0; i < n; i++) {
            const node = q.shift()
            if (node == null) {
                seenNull = true
            } else {
                
                if (seenNull || seenNullAbove) {
                    return false
                }
                
                q.push(node.left)
                q.push(node.right)
            }
        }
        seenNullAbove = seenNull
    }
    return true
};

var isCompleteTree = function(root) {
    const q = [root]
    while (q.length > 0) {
        const n = q.length
        const row = []
        for (let i = 0; i < n; i++) {
            const node = q.shift()
            if (node == null) {
                return q.filter(x => x != null) == 0
            }
            row.push(node)
            q.push(node.left)
            q.push(node.right)
        }
    }
    return true
};

/*
    when we dequeue the first null, stop and check if the remaining queue only contains nulls
*/
var isCompleteTree = function(root) {
    const q = [root]
    while (q.length > 0) {
        const node = q.shift()
        if (node == null) {
            return q.filter(x => x != null) == 0
        }
        q.push(node.left)
        q.push(node.right)
    }
    return true
};