class Heap {
  constructor() {
    this.arr = []
  }

  heapify(values) {
    // O(nlogn) version
    for (let i = 0; i < values.length; i++) {
      this.heapPush(values[i])
    }
    /*
      O(n) version
      bottom-up
      shift down from bottom to up such that we minimize the number of shift operations
      n/2 + n/8 + n/16.... = O(n)
    */
    this.arr = values
    const n = values.length
    for (let i = Math.floor(n / 2); i >= 0; i--) {
      this._shiftDown(i)
    }
  }

  heapPush(value) {
    this.arr.push(value)
    let curIdx = this.arr.length - 1
    this._shiftUp(curIdx)
  }

  heapPop() {
    const temp = this.arr[0]
    this.arr[0] = this.arr[this.arr.length - 1]
    this.arr[this.arr.length - 1] = temp
    const p = this.arr.pop()
    this._shiftDown(0)
    return p
  }

  // used by heapify, pop
  _shiftDown(fromIdx) {
    let cur = fromIdx
    while (cur < this.arr.length) {
      const left = cur * 2 + 1
      const right = cur * 2 + 2
      if (left < this.arr.length && right < this.arr.length) {
        if (this.arr[cur] < this.arr[left] && this.arr[cur] < this.arr[right]) {
          break
        } else if (this.arr[left] < this.arr[right]) {
          const temp = this.arr[cur]
          this.arr[cur] = this.arr[left]
          this.arr[left] = temp
          cur = left
        } else {
          const temp = this.arr[cur]
          this.arr[cur] = this.arr[right]
          this.arr[right] = temp
          cur = right
        }
      } else if (left < this.arr.length) {
        if (this.arr[left] < this.arr[cur]) {
          const temp = this.arr[cur]
          this.arr[cur] = this.arr[left]
          this.arr[left] = temp
          cur = left
        }
        break
      } else {
        break
      }
    }
  }

  // used by push
  _shiftUp(fromIdx) {
    let curIdx = fromIdx
    while (curIdx > 0) {
      const parentIdx = Math.floor((curIdx - 1) / 2)
      if (this.arr[parentIdx] > this.arr[curIdx]) {
        const temp = this.arr[curIdx]
        this.arr[curIdx] = this.arr[parentIdx]
        this.arr[parentIdx] = temp
        curIdx = parentIdx
      } else {
        break
      }
    }
  }
}

// unique values
let h = new Heap()
h.heapPush(8)
h.heapPush(9)
h.heapPush(6)
h.heapPush(7)
h.heapPush(4)
h.heapPush(3)
h.heapPush(5)
console.log(h.arr)
while (h.arr.length > 0) {
  console.log(h.heapPop())
}

// duplicate values
h = new Heap()
h.heapPush(8)
h.heapPush(8)
h.heapPush(6)
h.heapPush(4)
h.heapPush(4)
h.heapPush(3)
h.heapPush(5)
console.log(h.arr)
while (h.arr.length > 0) {
  console.log(h.heapPop())
}

console.log("-------------------------")

// unique values
h = new Heap()
h.heapify([6, 4, 2, 8, 9, 5, 7, 3])
let res = []
while (h.arr.length > 0) {
  res.push(h.heapPop())
}
console.log(res)

// duplicate values
h = new Heap()
h.heapify([6, 4, 2, 8, 9, 5, 7, 4])
res = []
while (h.arr.length > 0) {
  res.push(h.heapPop())
}
console.log(res)

console.log("-------------------------")

// Heap Sort
function heapsort(values) {
  const res = []
  const h = new Heap()
  h.heapify(values)
  const n = values.length
  for (let i = 0; i < n; i++) {
    res.push(h.heapPop())
  }
  return res
}

console.log(heapsort([12, 3, 1, 2, 4, 6, 3, 2, 4, 6, 3, 37, 37, 5, 5, 7, 77, 33, 4, 45]))