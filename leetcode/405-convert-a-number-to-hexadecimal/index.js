var toHex = function(num) {
    if (num == 0) {
        return '0'
    }
    if (num < 0) {
        num += 2**32
    }
    let res = ''
    while (num > 0) {
        const d = num % 16
        if (d < 10) {
            res = `${d}` + res
        } else {
            const m = {
                10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'
            }
            res = m[d] + res
        }
        num = Math.floor(num / 16)
    }
    return res
};