/*
    closure
*/
var createCounter = function(n) {
    let val = n
    return function() {
        res = val
        val += 1
        return res
    };
};

/*
    n++ vs ++n
*/
var createCounter = function(n) {
    let val = n
    return function() {
        return val++
    };
};