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
    constructor(capacity) {
        this.cap = capacity
        this.ht = {}
        this.htSize = 0
        this.head = new DLLNode()
        this.tail = new DLLNode()
        this.head.next = this.tail
        this.tail.prev = this.head
    }
    _removeNode(node) {
        node.prev.next = node.next
        node.next.prev = node.prev
    }
    _addToTail(node) {
        const last = this.tail.prev
        last.next = node
        node.prev = last
        node.next = this.tail
        this.tail.prev = node
    }
    get(key) {
        if (key in this.ht === false) {
            return -1
        }
        const node = this.ht[key]
        this._removeNode(node)
        this._addToTail(node)
        return node.val
    }
    put(key, value) {
        if (key in this.ht) {
            const node = this.ht[key]
            node.val = value
            this._removeNode(node)
            this._addToTail(node)
        } else {
            const newNode = new DLLNode(key, value)
            this._addToTail(newNode)
            this.ht[key] = newNode
            this.htSize += 1
        }
        if (this.htSize > this.cap) {
            const first = this.head.next
            this._removeNode(first)
            delete this.ht[first.key]
            this.htSize -= 1
        }
    }
}

/*
    2nd: use JS built-in ES6 Map()
    
    Time  put:O(1), get: O(1)
*/
class LRUCache {
    constructor(capacity) {
        this.cap = capacity
        this.map = new Map()
    }
    get(key) {
        if (this.map.has(key) === false) {
            return -1
        }
        const value = this.map.get(key)
        this.map.delete(key)
        this.map.set(key, value)
        return value
    }
    put(key, value) {
        if (this.map.has(key)) {
            this.map.delete(key)
        }
        this.map.set(key, value)
        if (this.map.size > this.cap) {
            const oldest = this.map.keys().next().value
            this.map.delete(oldest)
        }
    }
}

/** 
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */