/*
    1st: sort by unit, take as many as boxes until truckSize = 0

    Time    O(NlogN)
    Space   O(1)
    156 ms, faster than 100.00%
*/
var maximumUnits = function(boxTypes, truckSize) {
    boxTypes.sort((a, b) => b[1] - a[1])
    let units = 0
    for (let [cnt, u] of boxTypes) {
        if (truckSize >= cnt) {
            truckSize -= cnt
            units += cnt * u
        } else {
            units += truckSize * u
            truckSize = 0
        }
    }
    return units
};