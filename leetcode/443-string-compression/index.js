/*
    1st approach: cache the result and put it back in the input

    Time    O(n)
    Space   O(n)
    80 ms, faster than 95.07%
*/
var compress = function(chars) {
    if (chars.length == 0) { return '' }
    const res = []
    let count = 1
    let cur = chars.shift()
    while (chars.length > 0) {
        const c = chars.shift()
        if (c == cur) {
            count += 1
        } else {
            res.push([cur, count])
            cur = c
            count = 1
        }
    }
    res.push([cur, count])
    
    while (res.length > 0) {
        const [cur, count] = res.shift()
        if (count == 1) {
            chars.push(cur)
        } else {
            chars.push(cur)
            chars.push(...`${count}`)
        }
    }
    return chars.length
};

/*
    2nd
    
    Time    O(N)
    Space   O(N)
*/
var compress = function(chars) {
    let cur = chars[0]
    let cnt = 1
    const temp = []
    for (let i = 1; i < chars.length; i++) {
        const x = chars[i]
        if (cur == x) {
            cnt += 1
        } else {
            temp.push({cur, cnt})
            cur = x
            cnt = 1
        }
    }
    temp.push({cur, cnt})
    let res = ''
    for (let {cur, cnt} of temp) {
        res += cur
        if (cnt > 1) {
            res += `${cnt}`
        }
    }
    const A = res.split('')
    for (let i = 0; i < A.length; i++) {
        chars[i] = A[i]
    }
    return A.length
};