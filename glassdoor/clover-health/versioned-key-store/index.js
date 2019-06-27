/*
    lc981
    
    Create a timebased key-value store class TimeMap, that supports two operations.

    1. set(string key, string value, int timestamp)

    Stores the key and value, along with the given timestamp.
    2. get(string key, int timestamp)

    Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
    If there are multiple such values, it returns the one with the largest timestamp_prev.
    If there are no values, it returns the empty string ("").

    Time    O(nlogk)
    Space   O(nk)
    484 ms, faster than 97.16%
*/

/**
 * Initialize your data structure here.
 */
var TimeMap = function () {
    this.m = {}
};

/** 
 * @param {string} key 
 * @param {string} value 
 * @param {number} timestamp
 * @return {void}
 */
TimeMap.prototype.set = function (key, value, timestamp) {
    if (this.m[key] === undefined) {
        this.m[key] = [[timestamp, value]]
    } else {
        this.m[key].push([timestamp, value])
    }
};

/** 
 * @param {string} key 
 * @param {number} timestamp
 * @return {string}
 */
TimeMap.prototype.get = function (key, timestamp) {
    if (this.m[key] === undefined) {
        return ""
    }
    const idx = this._bsearch(this.m[key], timestamp)
    if (idx < 0) {
        return ""
    }
    return this.m[key][idx]
};

TimeMap.prototype._bsearch = function (arr, timestamp) {
    let left = 0
    let right = arr.length - 1
    while (left <= right) {
        const mid = Math.floor((left + right) / 2)
        if (timestamp < arr[mid][0]) {
            right = mid - 1
        } else if (timestamp > arr[mid][0]) {
            left = mid + 1
        } else {
            return mid
        }
    }
    return right
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */