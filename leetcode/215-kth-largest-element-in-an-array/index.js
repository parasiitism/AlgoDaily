/*
    1st approach: Priority Queue

    Time    O(n * (logk + k)) since insert takes O(k)
    Space   O(k)
    88 ms, faster than 62.47% 
*/
var findKthLargest = function(nums, k) {
    const n = nums.length
    const kk = n - k + 1
    if (k < kk) {
        const minheap = new MyPriorityQueue()
        for (let x of nums) {
            minheap.push(x)
            if (minheap.size() > k) {
                minheap.pop()
            }
        }
        return minheap.A[0]
    }
    const maxheap = new MyPriorityQueue()
    for (let x of nums) {
        maxheap.push(-x)
        if (maxheap.size() > kk) {
            maxheap.pop()
        }
    }
    return -maxheap.A[0]
};

class MyPriorityQueue {
    constructor() {
        this.A = []
    }
    size() {
        return this.A.length
    }
    push(x) {
        this.A.push(x)
        this._shiftUp(this.A.length-1)
    }
    _shiftUp(idx) {
        const parentIdx = Math.floor((idx-1)/2)
        if (parentIdx >= 0 && this.A[idx] < this.A[parentIdx]) {
            [this.A[idx], this.A[parentIdx]] = [this.A[parentIdx], this.A[idx]];
            this._shiftUp(parentIdx)
        }
    }
    pop() {
        const n = this.A.length;
        [this.A[0], this.A[n-1]] = [this.A[n-1], this.A[0]];
        const top = this.A.pop()
        this._shiftDown(0)
        return top
    }
    _shiftDown(idx) {
        const children = [idx*2+1, idx*2+2]
        let targetIdx = idx
        for (let i of children) {
            if (i < this.A.length && this.A[i] < this.A[targetIdx]) {
                targetIdx = i
            }
        }
        if (targetIdx > idx) {
            [this.A[idx], this.A[targetIdx]] = [this.A[targetIdx], this.A[idx]];
            this._shiftDown(targetIdx)
        }
    }
}