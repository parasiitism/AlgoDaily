var toHex = function(num) {
    if (num == 0) {
        return '0'
    }
    if (num < 0) {
        num += 2**32
    }
    const res = []
    while (num > 0) {
        const d = num % 16
        if (d < 10) {
            res.push(`${d}`)
        } else {
            const alphabet = 'abcdef'
            res.push(alphabet[d%10])
        }
        num = Math.floor(num / 16)
    }
    return res.reverse().join('')
};