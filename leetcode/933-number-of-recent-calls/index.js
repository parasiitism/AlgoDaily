class RecentCounter {
    constructor() {
        this.times = []
    }
    ping(t) {
        this.times.push(t)
        while (this.times.length > 0 && t - this.times[0] > 3000) {
            this.times.shift()
        }
        return this.times.length
    }
}

/** 
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = new RecentCounter()
 * var param_1 = obj.ping(t)
 */