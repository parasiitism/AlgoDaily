/*
    binary search
*/
Array.prototype.upperBound = function(target) {
    let left = 0
    let right = this.length
    while (left < right) {
        const mid = Math.floor((left + right) / 2)
        if (target < this[mid]) {
            right = mid
        } else {
            left = mid + 1
        }
    }
    if (this[left-1] != target) {
        return -1
    }
    return left-1
};


// [3,4,5].upperBound(5); // 2
// [1,4,5].upperBound(2); // -1
// [3,4,6,6,6,6,7].upperBound(6) // 5