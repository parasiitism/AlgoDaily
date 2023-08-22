/*
    1st: prototype with Object
    - timeout_ID = setTimeout(...)
    - clearTimeout(timeout_ID)
*/
class TimeLimitedCache {
    constructor() {
        this.cache = {}     // key: value
        this.timeouts = {}  // key: timeout id
    }
    set(key, value, duration) {
        let didExisted = key in this.cache
        if (didExisted) {
            delete this.cache[key]
            const timeoutID = this.timeouts[key]
            clearTimeout(timeoutID)
            delete this.timeouts[key]
        }
        this.cache[key] = value
        this.timeouts[key] = setTimeout(() => {
            delete this.cache[key]
            const timeoutID = this.timeouts[key]
            clearTimeout(timeoutID)
            delete this.timeouts[key]
        }, duration)
        return didExisted
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