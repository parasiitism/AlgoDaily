/*
    2nd: queue + hashtable
    - not a very optimal approach
    - counter the occurence of each number
    - when we do showFirstUnique(), pop the queue until we reach to a number which appears once only

    Time of init                O(N)
    Time of showFirstUnique()   O(N)
    Time of add()               O(1)
    Space                       O(N)
    1064 ms, faster than 23.39%
*/
class FirstUnique {
    constructor(nums) {
        this.counter = {}
        this.queue = []
        
        for (let x of nums) {
            if ((x in this.counter) == false) {
                this.counter[x] = 0
            }
            this.counter[x] += 1
        }
        
        for (let x of nums) {
            if (this.counter[x] == 1) {
                this.queue.push(x)
            }
        }
    }
    showFirstUnique() {
        this._findUnique()
        if (this.queue.length > 0) {
            return this.queue[0]
        }
        return -1
    }
    add(x) {
        if (x in this.counter) {
            this.counter[x] += 1
        } else {
            this.counter[x] = 1
            this.queue.push(x)
        }
    }
    _findUnique() {
        while (
            this.queue.length > 0 &&
            this.counter[this.queue[0]] > 1
        ) {
            this.queue.shift()
        }
    }
}

/*
    3rd: array + hashtable

    Time of init                O(N)
    Time of showFirstUnique()   O(N)
    Time of add()               O(1)
    Space                       O(N)
    376 ms, faster than 79.03%
*/
class FirstUnique {
    constructor(nums) {
        this.ctr = {}
        this.order = []
        this.cursor = 0
        for (let x of nums) {
            if (x in this.ctr === false) {
                this.ctr[x] = 0
                this.order.push(x)
            }
            this.ctr[x] += 1
        }
    }
    showFirstUnique() {
        while (this.ctr[this.order[this.cursor]] > 1) {
            this.cursor += 1
        }
        if (this.cursor == this.order.length) {
            return -1
        }
        return this.order[this.cursor]
    }
    add(x) {
        if (x in this.ctr === false) {
            this.ctr[x] = 0
            this.order.push(x)
        }
        this.ctr[x] += 1
    }
}