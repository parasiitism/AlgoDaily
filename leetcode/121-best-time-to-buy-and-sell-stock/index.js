/**
 * @param {number[]} prices
 * @return {number}
 * 
 * 
 *  1st approach: classic dp problem
    - keep the dip when we traverse the list
    - when there is a new peak and the current diff is larger than the previous diff, update the diff
    
 * 52 ms, faster than 95.20%
 */
var maxProfit = function (prices) {
    let dip = Number.MAX_VALUE
    let res = 0
    for (let i = 0; i < prices.length; i++) {
        dip = Math.min(dip, prices[i])
        res = Math.max(res, prices[i] - dip)
    }
    return res
};