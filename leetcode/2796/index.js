String.prototype.replicate = function(times) {
    let res = []
    for (let i = 0; i < times; i++) {
        res.push(this)
    }
    return res.join('')
}