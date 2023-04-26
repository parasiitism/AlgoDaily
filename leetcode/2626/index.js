var reduce = function(nums, fn, init) {
    let accumator = init
    for (let x of nums) {
        accumator = fn(accumator, x)
    }
    return accumator
};