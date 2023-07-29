/*
    A process tree has crashed and you are given a sequence of it's nodes in random order, 
    seach representing a process and possible child(s). 
    Each node has at most two child process. Find the root process node

    Input:
    {5 : [], 1: [2, 3], 4 : [], 3: [6], 6 : [], 2 : [4, 5]}

     			1
            /      \
        2            3
    /     \          / 
    4     5         6

    ===== solutions =====
    - Find the indegree of every node
*/
const findRoot = (parentChildren) => {
    const indegree = {}
    for (let parent in parentChildren) {
        if (parent in indegree == false) {
            indegree[parent] = 0
        }
        const children = parentChildren[parent]
        for (let child of children) {
            if (child in indegree == false) {
                indegree[child] = 0
            }
            indegree[child] += 1
        }
    }
    for (let node in indegree) {
        if (indegree[node] == 0) {
            return node
        }
    }
    return -1
}

let a = {5 : [], 1: [2, 3], 4 : [], 3: [6], 6 : [], 2 : [4, 5]}
console.log(findRoot(a))