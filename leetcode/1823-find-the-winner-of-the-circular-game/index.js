/*
    1st: linked list

    Time    O(N)
    Space   O(N) the linked list
    180 ms, faster than 33.51%
*/
var findTheWinner = function(n, k) {
    if (k == 1) {
        return n
    }
    const circleHead = new LLNode(1)
    let cur = circleHead
    for (let i = 2; i <= n; i++) {
        cur.next = new LLNode(i)
        cur = cur.next
    }
    cur.next = circleHead
    cur = circleHead
    while (cur.next !== cur) {
        for (let i = 1; i < k-1; i++) {
            cur = cur.next
        }
        cur.next = cur.next.next
        cur = cur.next
    }
    return cur.val
};

class LLNode {
    constructor(val = 0) {
        this.val = val
        this.next = null
    }
}