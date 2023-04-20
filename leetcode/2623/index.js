/*
    JS closure
    - ...arg: rest parameters
    - hashtable
*/

/**
 * @param {Function} fn
 */
function memoize(fn) {
    const seen = {}

    const gen_key = args => {
        let strs = args.map(x => JSON.stringify(x))
        return strs.join(',')
    } 

    return function(...args) {
        const key = gen_key(args)
        if (key in seen) {
            return seen[key]
        }
        const res = fn(...args)
        seen[key] = res
        return res
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */