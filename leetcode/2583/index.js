/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthLargestLevelSum = function(root, k) {
    const minheap = new MinHeap()
    const q = [root]
    while (q.length > 0) {
        const n = q.length
        let levelSum = 0
        for (let _ = 0; _ < n; _++) {
            const node = q.shift()
            levelSum += node.val
            if (node.left) {
                q.push(node.left)
            }
            if (node.right) {
                q.push(node.right)
            }
        }
        minheap.push(levelSum)
        if (minheap.A.length > k) {
            minheap.pop()
        }
    }
    if (minheap.A.length < k) {
        return -1
    }
    return minheap.pop()
};

class MinHeap {
    constructor() {
        this.A = []
    }
    push(x) {
        this.A.push(x)
        this._shiftUp(this.A.length-1)
    }
    pop() {
        const n = this.A.length;
        [this.A[0], this.A[n-1]] = [this.A[n-1], this.A[0]];
        const popped = this.A.pop()
        this._shiftDown(0)
        return popped
    }
    _shiftUp(i) {
        const parentIdx = Math.floor((i-1)/2)
        if (parentIdx >= 0 && this.A[i] < this.A[parentIdx]) {
            [this.A[i], this.A[parentIdx]] = [this.A[parentIdx], this.A[i]];
            this._shiftUp(parentIdx)
        }
    }
    _shiftDown(i) {
        const children = [i*2+1, i*2+2]
        let minChildIdx = i
        for (let child of children) {
            if (child >= this.A.length) { continue }
            if (this.A[child] < this.A[minChildIdx]) {
                minChildIdx = child
            }
        }
        if (minChildIdx != i) {
            [this.A[i], this.A[minChildIdx]] = [this.A[minChildIdx], this.A[i]];
            this._shiftDown(minChildIdx)
        }
    }
}