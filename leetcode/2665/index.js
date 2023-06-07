/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {

    const init_val = init
    let cur_val = init

    const increment = () => {
        cur_val += 1
        return cur_val
    }

    const decrement = () => {
        cur_val -= 1
        return cur_val
    }

    const reset = () => {
        cur_val = init_val
        return cur_val
    }

    return {
        increment,
        decrement,
        reset,
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */