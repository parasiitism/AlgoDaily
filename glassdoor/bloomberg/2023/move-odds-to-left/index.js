/*
    Given an array, move all the odds to the left, while maintaining the original order of the numbers

    Input: [1,2,3,4,5,6,7,8,9]
    Output: [1,3,5,7,9,x,x,x,x] e.g. [1, 3, 5, 7, 9, 6, 4, 8, 2]
*/
var moveOddsToLeftButIgnoreOrderOfEvens = function(A) {
    let j = 0
    for (let i = 0; i < A.length; i++) {
        if (A[i] % 2 == 1) {
            [A[i], A[j]] = [A[j], A[i]];
            j += 1
        }
    }
};
let a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
moveOddsToLeftButIgnoreOrderOfEvens(a)
console.log(a)

console.log("--- followup: now we also care about the order of evens ---")

class LLNode {
    constructor(val=0) {
        this.val = val
        this.next = null
    }
}

var moveOddsToLeftWithEvensInOrder = function(A) {
    const dummy = new LLNode()
    let cur = dummy
    for (let i = 0; i < A.length; i++) {
        cur.next = new LLNode(A[i])
        cur = cur.next
    }
    let slow = dummy
    let fast = dummy
    while (fast != null && fast.next != null) {
        if (fast.next.val % 2 == 1) {
            const next = fast.next
            fast.next = fast.next.next
            const orignal_slow_next = slow.next
            slow.next = next
            next.next = orignal_slow_next
            slow = slow.next
        }
        fast = fast.next
    }
    cur = dummy.next
    for (let i = 0; i < A.length; i++) {
        A[i] = cur.val
        cur = cur.next
    }
};
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
moveOddsToLeftWithEvensInOrder(a)
console.log(a)