/*
    1st approach: hashtable

    Time    O(1)
    Space   O(n)
    204 ms, faster than 38.40%
*/
class Logger {
    constructor() {
        this.ht = {}
    }
    shouldPrintMessage(timestamp, message) {
        if (message in this.ht == false) {
            this.ht[message] = timestamp
            return true
        }
        const prevTime = this.ht[message]
        if (timestamp < prevTime+10) {
            return false
        }
        this.ht[message] = timestamp
        return true
    }
}

/**
 * Your Logger object will be instantiated and called as such:
 * var obj = new Logger()
 * var param_1 = obj.shouldPrintMessage(timestamp,message)
 */
