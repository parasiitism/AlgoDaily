/*
    array

    Time    O(N)
    Space   O(1)
*/
var numberOfEmployeesWhoMetTarget = function(hours, target) {
    let res = 0
    for (let h of hours) {
        if (h >= target) {
            res += 1
        }
    }
    return res
};