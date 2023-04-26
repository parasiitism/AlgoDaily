/*
    recursion
*/
var curry = function(fn) {
    return function curried(...args) {
        if (args.length === fn.length) {
            return fn(...args);
        }
        return function (...otherArgs) {
            // keep adding paramters to the function
            return curried(...args, ...otherArgs);
        };
    };
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */