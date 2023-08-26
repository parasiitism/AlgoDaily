/*
    2nd approach: optimize the above approach
    - find the minNode
    - there are 2 cases to insert a node
        1. cur <= target < cur.next
        2. cur.next == head and insertion no yet happen

    Time    O(2N)
    Space   O(1)
    92 ms, faster than 27.43%
*/
var insert = function(head, insertVal) {
    const newNode = new Node(insertVal)
    if (head == null) {
        newNode.next = newNode
        return newNode
    }
    let prev = head
    let curr = head.next
    while (true) {
        if (prev.val <= insertVal && insertVal <= curr.val) {
            break
        }
        if (prev.val > curr.val) {
            if (prev.val <= insertVal || insertVal <= curr.val) {
                break
            }
        }
        prev = curr
        curr = curr.next
        if (prev == head) {
            break
        }
    }
    prev.next = newNode
    newNode.next = curr
    return head
};