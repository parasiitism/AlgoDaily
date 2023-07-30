/*
    1st: Doubly linked list

    Time of init    O(N)
    Time of fetch   O(K) at most O(N)
    177ms beats 49.02%
*/
class DLLNode {
    constructor(val=-1) {
        this.val = val
        this.prev = null
        this.next = null
    }
}

class MRUQueue {
    constructor(n) {
        this.n = n
        this.head = new DLLNode()
        this.tail = new DLLNode()
        this.head.next = this.tail
        this.tail.prev = this.head
        for (let i = 1; i <= n; i++) {
            const node = new DLLNode(i)
            this._addNodeToTail(node)
        }
    }
    _removeFromList(node) {
        node.prev.next = node.next
        node.next.prev = node.prev
    }
    _addNodeToTail(node) {
        const last = this.tail.prev
        last.next = node
        node.prev = last
        node.next = this.tail
        this.tail.prev = node
    }
    fetch(k) {
        let targetNode = null
        let cnt = 0
        let cur = this.head.next
        while (cur != null) {
            cnt += 1
            if (cnt == k) {
                targetNode = cur
                break
            }
            cur = cur.next
        }
        this._removeFromList(targetNode)
        this._addNodeToTail(targetNode)
        return targetNode.val
    }
}

/** 
 * Your MRUQueue object will be instantiated and called as such:
 * var obj = new MRUQueue(n)
 * var param_1 = obj.fetch(k)
 */