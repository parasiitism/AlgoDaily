/*
    2nd: class with Object
    - timeout_ID = setTimeout(...)
    - clearTimeout(timeout_ID)
*/
class TimeLimitedCache {

    key2values: object
    key2timeoutIDs: object

    constructor() {
        this.key2values = {}
        this.key2timeoutIDs = {}
    }

    set(key: number, value: number, duration: number): boolean {
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
    }

    get(key: number): number {
        if (key in this.key2values === false) {
            return -1
        }
        return this.key2values[key]
    }

	count(): number {
        return Object.keys(this.key2values).length
    }
}

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */