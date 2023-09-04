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

/*
    2nd prototype with Object
    - we can optimize 1st with only one hashtable
*/
class TimeLimitedCache {
    constructor() {
        this.cache = {}     // key: { value, timeoutID }
    }
    set(key, value, duration) {
        let didExisted = key in this.cache
        if (didExisted) {
            clearTimeout(this.cache[key].timeoutID)
        }
        const timeoutID = setTimeout(() => {
            delete this.cache[key]
        }, duration)
        this.cache[key] = { value, timeoutID }
        return didExisted
    }
    get(key) {
        if (key in this.cache == false) {
            return -1
        }
        return this.cache[key].value
    }
    count() {
        return Object.keys(this.cache).length
    }
}

/*
    2nd prototype with ES6 Map
    - we can optimize 1st with only one hashtable
*/
class TimeLimitedCache {
    constructor() {
        this.cache = new Map() // key: {value, timeoutID}
    }
    set(key, value, duration) {
        const isExisted = this.cache.has(key)
        if (isExisted) {
            const timeoutID = this.cache.get(key).timeoutID
            clearTimeout(timeoutID)
        }
        const timeoutID = setTimeout(() => {
            this.cache.delete(key)
        }, duration)
        this.cache.set(key, { value, timeoutID })
        return isExisted
    }
    get(key) {
        if (!this.cache.has(key)) {
            return -1
        }
        return this.cache.get(key).value
    }
    count() {
        return this.cache.size
    }
}