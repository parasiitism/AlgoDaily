/*
    1st
*/

/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {

    let pending = false
    let pending_args = null

    const callbackFn = () => {
        if (pending) {
            fn(...pending_args)
            pending_args = null
            setTimeout(callbackFn, t)
        }
    }

    return function(...args) {
        if (pending_args === null) {
            pending_args = args
            return
        }
        fn(...args)
        pending = true
        setTimeout(callbackFn, t)
    }
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */

/*
    2nd
*/
var throttle = function(fn, t) {
    
    let pending = false
    let pending_args = null
    
    const wrapperFn = function(...args) {
        if (!pending) {
            pending_args = null
            pending = true
            fn(...args)

            setTimeout(() => {
                pending = false;
                if (pending_args !== null) {
                    wrapperFn(...pending_args);
                }
            }, t);
        } else {
            pending_args = args
        }
    }
    return wrapperFn
};

/*
    Use Date.now()
*/
var throttle = function(fn, t) {
    let nextTime = 0
    let curTimeout = null
    return (...args) => {
        const delay = Math.max(0, nextTime - Date.now())
        clearTimeout(curTimeout) // meaning that the calls in-between are cancelled
        curTimeout = setTimeout(() => {
            fn(...args)
            nextTime = Date.now() + t
        }, delay)
    }
};