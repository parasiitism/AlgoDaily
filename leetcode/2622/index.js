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
    set(key, val, duration) {
        const existed = key in this.cache
        if (existed) {
            const tID = this.timeouts[key]
            delete this.timeouts[key]
            clearTimeout(tID)
        }
        this.cache[key] = val
        const tID = setTimeout(() => {
            delete this.cache[key]
            delete this.timeouts[key]
        }, duration)
        this.timeouts[key] = tID
        return existed
    }
    get(key) {
        if (key in this.cache == false) {
            return -1
        }
        return this.cache[key]
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