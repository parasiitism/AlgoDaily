/*
    setTimeout and clearTimeout
*/
var debounce = function(fn, t) {

    let pending_timeout = null

    return function(...args) {

        if (pending_timeout !== null) {
            clearTimeout(pending_timeout)
            pending_timeout = null
        }

        const timeout_id = setTimeout(() => {
            fn(...args)
            pending_timeout = null
        }, t)
        pending_timeout = timeout_id
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */