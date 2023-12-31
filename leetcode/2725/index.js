/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    fn(...args)
    let ref = setInterval(() => fn(...args), t)
    return function() {
        clearInterval(ref)
    }
};