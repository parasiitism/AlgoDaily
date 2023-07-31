/*
    1st: save the minValue for every item
    - for each push(), calculate the curMin and put it with the x in stack
    - for each pop(), pop the top item

    Time    O(1)
    Space   O(n)
    100ms beats 85.92%
*/
class MinStack {
	constructor() {
        this.stack = [] // [cur, min]
    }
    push(val) {
        const n = this.stack.length
        if (this.stack.length > 0 && this.stack[n-1][1] < val) {
            const min = this.stack[n-1][1]
            this.stack.push([val, min])
        } else {
            this.stack.push([val, val])
        }
    }
    pop() {
        return this.stack.pop()
    }
    top() {
        return this.stack[this.stack.length-1][0]
    }
    getMin() {
        return this.stack[this.stack.length-1][1]
    }
}
