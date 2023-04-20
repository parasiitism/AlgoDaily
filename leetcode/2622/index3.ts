/*
    3nd: class with Map
    - timeout_ID = setTimeout(...)
    - clearTimeout(timeout_ID)
    - this.key2values.size <> Object.keys(this.key2values).length
*/
class TimeLimitedCache {

    key2values: Map<number, number>
    key2timeoutIDs: Map<number, any>

    constructor() {
        this.key2values = new Map()
        this.key2timeoutIDs = new Map()
    }

    set(key: number, value: number, duration: number): boolean {
        let is_existed = false
        if (this.key2values.has(key)) {
            is_existed = true
            const old_timeout_ID = this.key2timeoutIDs.get(key)
            clearTimeout(old_timeout_ID)
        }
        // this.key2values[key] = value
        this.key2values.set(key, value) 
        const timeoutID = setTimeout(() => {
            // delete this.key2values[key]
            // delete this.key2timeoutIDs[key]
            this.key2values.delete(key)
            this.key2timeoutIDs.delete(key)
        }, duration)
        this.key2timeoutIDs.set(key, timeoutID)
        return is_existed
    }

    get(key: number): number {
        if (!this.key2values.has(key)) {
            return -1
        }
        return this.key2values.get(key)
    }

	count(): number {
        return this.key2values.size
    }
}

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */