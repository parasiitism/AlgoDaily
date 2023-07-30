/*
    1st approach
    - count num: freq into a hashtable
    - put the hashtable key&value into a priority queue
    - the first k elements are the top k elements in the priority queue

    Time    O(NlogN)
    Space   O(N)
    56 ms, faster than 99.52%
*/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const ctr = {};
    nums.forEach(x => {
        if (x in ctr === false) {
            ctr[x] = 0
        }
        ctr[x] += 1
    })
    const arr = [];
    for (let key in ctr) {
        arr.push([ctr[key], key]);
    }
    arr.sort((a, b) => b[0] - a[0]);
    const res = []
    const n = Math.min(arr.length, k)
    for (let i = 0; i < n; i++) {
        res.push(arr[i][1])
    }
    return res
};
/*

*/
var topKFrequent = function(nums, k) {
    const ctr = {}
    for (let x of nums) {
        if (x in ctr === false) {
            ctr[x] = 0
        }
        ctr[x] += 1
    }
    const minheap = new MinHeap()
    for (let key in ctr) {
        const f = ctr[key]
        minheap.push(f, key)
        if (minheap.size() > k) {
            minheap.pop()
        }
    }
    const res = []
    for (let [_f, k] of minheap.A) {
        res.push(k)
    }
    return res
};

class MinHeap {
    constructor() {
        this.A = [] // [[freq, key]]
    }
    size() {
        return this.A.length
    }
    push(f, key) {
        this.A.push([f, key])
        this._shiftUp(this.A.length-1)
    }
    _shiftUp(i) {
        const parentIdx = Math.floor((i-1)/2)
        if (parentIdx >= 0 && this.A[i][0] < this.A[parentIdx][0]) {
            [this.A[i], this.A[parentIdx]] = [this.A[parentIdx], this.A[i]];
            this._shiftUp(parentIdx)
        }
    }
    _shiftDown(i) {
        const children = [i*2+1, i*2+2]
        let minChildIdx = i
        for (let j of children) {
            if (j >= this.A.length) { continue }
            if (this.A[j][0] < this.A[minChildIdx][0]) {
                minChildIdx = j
            }
        }
        if (minChildIdx > i) {
            [this.A[i], this.A[minChildIdx]] = [this.A[minChildIdx], this.A[i]];
            this._shiftDown(minChildIdx)
        }
    }
    pop() {
        const n = this.A.length;
        [this.A[0], this.A[n-1]] = [this.A[n-1], this.A[0]];
        const [minFreq, node] = this.A.pop()
        this._shiftDown(0)
        return [minFreq, node]
    }

}