/*
    2 pointers

    Time    O(N)
    Space   O(1)
    76 ms, faster than 95.16%
*/
var removeNthFromEnd = function(head, n) {
    const dummy = new ListNode()
    dummy.next = head
    let slow = dummy
    let fast = dummy
    for (let i = 0; i < n; i++) {
        fast = fast.next
    }
    while (fast.next !== null) {
        slow = slow.next
        fast = fast.next
    }
    slow.next = slow.next.next
    return dummy.next
};