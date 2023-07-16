/*
    1st: prototype with Object
    - timeout_ID = setTimeout(...)
    - clearTimeout(timeout_ID)
*/
class TimeLimitedCache {
    constructor() {
        this.cache = {}
        this.timeouts = {} 
    }
    set(key, value, duration) {
        const ifExisted = key in this.cache
        if (ifExisted) {
            clearTimeout(this.timeouts[key])
            delete this.timeouts[key]
        }
        this.cache[key] = value
        this.timeouts[key] = setTimeout(() => {
            delete this.cache[key]
            clearTimeout(this.timeouts[key])
            delete this.timeouts[key]
        },duration)
        return ifExisted
    }
    get(key) {
        if (key in this.cache) {
            return this.cache[key]
        }
        return -1
    }
    count() {
        return Object.keys(this.cache).length
    }
}

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */