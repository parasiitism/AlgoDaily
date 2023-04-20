/*
    1st: prototype with Object
    - timeout_ID = setTimeout(...)
    - clearTimeout(timeout_ID)
*/

var TimeLimitedCache = function() {
    this.key2values = {}
    this.key2timeoutIDs = {}
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    let is_existed = false
    if (key in this.key2values) {
        is_existed = true
        const old_timeout_ID = this.key2timeoutIDs[key]
        clearTimeout(old_timeout_ID)
    }

    this.key2values[key] = value
    this.key2timeoutIDs[key] = setTimeout(() => {
        delete this.key2values[key];
        delete this.key2timeoutIDs[key]
    }, duration)
    return is_existed
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if (key in this.key2values === false) {
        return -1
    }
    return this.key2values[key]
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return Object.keys(this.key2values).length
};

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */