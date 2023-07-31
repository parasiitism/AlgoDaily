/*
    1st: hashtable
    - straight forward approach

    Insert Time				O(1)
	Remove Time				O(1)
	GetRandom Time		    O(N)
	Space					O(n) the unique keys
    244 ms, faster than 21.56%
*/
class RandomizedSet {
    constructor() {
        this.ht = new Set()
    }
    insert(x) {
        if (this.ht.has(x)) {
            return false
        }
        this.ht.add(x)
        return true
    }
    remove(x) {
        if (this.ht.has(x) == false) {
            return false
        }
        this.ht.delete(x)
        return true
    }
    getRandom() {
        const keys = Array.from(this.ht)
        const n = keys.length
        const i = Math.floor(Math.random() * n)
        return keys[i]
    }
}
/*
    hashtable + array, learned from others
	- save value: index in hashtable
	- when delete, swap the target item and the last item in the array, and remove the last item
    - see ./idea_add.png and ./idea_remove.png
    
    Insert Time				O(1)
	Remove Time				O(1)
	GetRandom Time		    O(1)
	Space					O(n) the unique keys
    120 ms beats 99.01%

    e.g.
    {
        a: 0,
        b: 1,
        c: 2,
        d: 3
    }
    [a, b, c, d]
    
    ---- remove 'b' ----

    step1:
    {
        a: 0,
        b: 3,
        c: 2,
        d: 1
    }
    [a, b, c, d]
    
    step2:
    {
        a: 0,
        b: 3, <- Important: remove the key and a non-existing index. We don't care about whether a key is pointing the exactly location  
        c: 2,
        d: 1
    }
    [a, c, d]

    step3:
    {
        a: 0,
        c: 2,
        d: 1
    }
    [a, c, d]
    
    ---- remove 'c' ----

    step1:
    {
        a: 0,
        c: 1,
        d: 2
    }
    [a, c, d]

    step2:
    {
        a: 0,
        c: 1,
        d: 2 <- remove
    }
    [a, d]

    step3:
    {
        a: 0,
        c: 1,
    }
    [a, d]
*/
class RandomizedSet {
    constructor() {
        this.ht = {}
        this.A = []
    }
    insert(val) {
        if (val in this.ht) { return false }
        this.ht[val] = this.A.length
        this.A.push(val)
        return true
    }
    remove(val) {
        if (val in this.ht === false) { return false }
        const idx = this.ht[val]

        const n = this.A.length
        const last = this.A[n-1];
        
        [this.A[idx], this.A[n-1]] = [this.A[n-1], this.A[idx]]
        this.ht[last] = idx

        this.A.pop()
        delete this.ht[val]

        return true
    }
    getRandom() {
        const i = Math.floor(Math.random() * this.A.length)
        return this.A[i]
    }
}