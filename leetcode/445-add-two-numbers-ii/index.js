/*
    1st approach: 2 stacks
	1. put the values into its corresponding stack
	2. pop the stacks, and sum up the numbers with carry
	3. if there is a carry, add 1

	Time	O(2m+2n)
	Space	O(m+n)
	140 ms, faster than 51.90%
*/
var addTwoNumbers = function(l1, l2) {
    
    const stack1 = getStack(l1)
    const stack2 = getStack(l2)
    
    let carry = 0;
	let cur = null
	while (stack1.length > 0 || stack2.length > 0 || carry > 0) {
		let a = 0;
		if (stack1.length > 0) {
			a = stack1.pop()
		}
		let b = 0;
		if (stack2.length > 0) {
			b = stack2.pop()
		}
		const sum = a + b + carry;
		carry = Math.floor(sum / 10);
		const newHead = new ListNode(sum % 10);
		newHead.next = cur
        cur = newHead
	}
	return cur;
};

const getStack = (l) => {
    const stack = []
    let cur = l
    while (cur !== null) {
        stack.push(cur.val)
        cur = cur.next
    }
    return stack
}

/*
    intuitive

    Time    O(A+B)
    Space   O(A+B)
*/
var addTwoNumbers = function(l1, l2) {
    const s1 = convert2stack(l1)
    const s2 = convert2stack(l2)
    const resFromRight = []
    let carry = 0
    while (s1.length > 0 || s2.length > 0) {
        let a = 0
        let b = 0
        if (s1.length > 0) {
            a = s1.pop()
        }
        if (s2.length > 0) {
            b = s2.pop()
        }
        const d = a + b + carry
        carry = Math.floor(d / 10)
        resFromRight.push(d % 10)
    }
    if (carry > 0) {
        resFromRight.push(carry)
    }
    const dumb = new ListNode()
    let cur = dumb
    while (resFromRight.length > 0) {
        cur.next = new ListNode(resFromRight.pop())
        cur = cur.next
    }
    return dumb.next
};

const convert2stack = head => {
    const stack = []
    let cur = head
    while (cur != null) {
        stack.push(cur.val)
        cur = cur.next
    }
    return stack
}