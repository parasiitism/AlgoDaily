/*
    1st: stack
    1. When we see a 'start'
        - pause the current function(if any), and update its execution time 
        - put the new start onto the stack
        - update the PREVIOUS TIME !!!
    2. When we see an 'end'
        - pop the current function from the stack, and update its execution time
        - increment the PREVIOUS TIME by one !!!
    
    To ask:
    - assume that the input must be a valid sequence of starts and ends?
    - input logs are sorted by timestamp?

    Time    O(N)
    Space   O(N/2) <- because there must be equal number of start and end
    76 ms, faster than 49.13%
*/
var exclusiveTime = function(n, logs) {
    const res = Array(n).fill(0)
    const stack = [] // fid
    let curTime = 0
    for (let i = 0; i < logs.length; i++) {
        const log = logs[i]
        let [fid, se, t] = log.split(':')
        fid = Number(fid)
        t = Number(t)
        if (se === 'start') {
            if (stack.length > 0) {
                const prevFid = stack[stack.length-1]
                res[prevFid] += t - curTime
            }
            curTime = t
            stack.push(fid)
        } else {
            const curFid = stack.pop()
            res[curFid] += t - curTime + 1
            curTime = t + 1
        }
    }
    return res
};