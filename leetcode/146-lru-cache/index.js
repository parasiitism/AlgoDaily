/*
    Doubly Linked List + Hashtable
    - similar to lc379, lc1429

    Time  put:O(1), get: O(1)
    196 ms, faster than 55.74%
*/
class DLLNode {
    constructor(key = -1, val = -1) {
        this.key = key
        this.val = val
        this.prev = null
        this.next = null
    }
}

class LRUCache {
    constructor(capacity = 0) {
        this.capacity = capacity
        this.ht = {}
        this.head = new DLLNode()
        this.tail = new DLLNode()
        this.head.next = this.tail
        this.tail.prev = this.head
        this.length = 0
    }
    _addToTail(node) {
        const last = this.tail.prev
        last.next = node
        node.prev = last
        node.next = this.tail
        this.tail.prev = node
    }
    _moveToTail(node) {
        node.prev.next = node.next
        node.next.prev = node.prev
        this._addToTail(node)
    }
    get(key) {
        if (key in this.ht == false) {
            return -1
        }
        const node = this.ht[key]
        this._moveToTail(node)
        return node.val
    }
    put(key, val) {
        if (key in this.ht == false) {
            const node = new DLLNode(key, val)
            this.ht[key] = node
            this._addToTail(node)
            this.length += 1
        } else {
            const node = this.ht[key]
            node.val = val
            this._moveToTail(node)
        }
        if (this.length > this.capacity) {
            const first = this.head.next
            first.prev.next = first.next
            first.next.prev = first.prev
            delete this.ht[first.key]
            this.length -= 1
        }
    }
}

/*
    2nd: use JS built-in ES6 Map()
    
    Time  put:O(1), get: O(1)
*/

/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
    this.cap = capacity
    this.map = new Map()
};

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
    if (this.map.has(key)) {
        const val = this.map.get(key)
        this.map.delete(key)
        this.map.set(key, val)
        return val
    }
    return -1
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
    if (this.map.has(key)) {
        this.map.delete(key)
    }
    this.map.set(key, value)
    if (this.map.size > this.cap) {
        const first = this.map.keys().next().value
        this.map.delete(first)
    }
};

/** 
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */