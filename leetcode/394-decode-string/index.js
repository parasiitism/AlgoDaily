/*
    1st approach: 2 stacks

    - 1st stack for counts
    - 2nd stack for substrings

    e.g. ab2[c3[de]]f

    when it comes to 2[
    cntStack = [2]
    strStack = ['ab', '']

    when it comes to 3[
    cntStack = [2, 3]
    strStack = ['ab', 'c', '']

    when it comes to the character before 1st ], 
    cntStack = [2, 3]
    strStack = ['ab', 'c', 'de']
    
    when it comes to 1st ], multiply 3 with 'de' and append to 'c'
    cntStack = [2]
    strStack = ['ab', 'cdedede']

    when it comes to 2nd ], , multiply 2 with 'cdedede' and append to 'abc'
    cntStack = []
    strStack = ['abcdededecdedede']

    when it comes to f
    cntStack = []
    strStack = ['abcdededecdededef']

    Time    O(n)
    Space   O(n)
    76 ms, faster than 68.48%
*/
var decodeString = function(s) {
    const count_stack = []
    const chars_stack = ['']
    let num = 0
    for (let c of s) {
        if (parseInt(c) >= 0 && parseInt(c) <= 9) {
            num = num * 10 + parseInt(c)
        } else if (c == '[') {
            chars_stack.push('')
            count_stack.push(num)
            num = 0
        } else if (c == ']') {
            const count = count_stack.pop()
            const sub = chars_stack.pop()
            chars_stack[chars_stack.length-1] += sub.repeat(count)
        } else {
            chars_stack[chars_stack.length-1] += c
        }
    }
    return chars_stack[0]
};

/*
    2nd approach: recursion + queue

    Time    O(2n)
    Space   O(n)
    108 ms, faster than 6.34%
*/
var decodeString = function(s) {
    const q = []
    for (let c of s) {
        q.push(c)
    }

    const dfs = () => {
        let res = ''
        let num = 0
        while (q.length > 0) {
            const c = q.shift()
            if (c >= '0' && c <= '9') {
                num = 10 * num + parseInt(c)
            } else if (c === '[') {
                const sub =  dfs()
                res += sub.repeat(num)
                num = 0
            } else if (c === ']') {
                break
            } else {
                res += c
            }
        }
        return res
    }
    return dfs()
};

/*
    3rd approach: recursion + string iteration with a global index

    Time    O(n)
    Space   O(n)
    58 ms, faster than 56.11%
*/
var decodeString = function(s) {
    let idx = 0
    const dfs = () => {
        let res = ''
        let num = 0
        while (idx < s.length) {
            const c = s[idx]
            idx += 1
            if (c >= '0' && c <= '9') {
                num = 10 * num + parseInt(c)
            } else if (c === '[') {
                const sub =  dfs()
                res += sub.repeat(num)
                num = 0
            } else if (c === ']') {
                break
            } else {
                res += c
            }
        }
        return res
    }
    return dfs()
};