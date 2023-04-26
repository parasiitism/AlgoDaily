/*
    1st: iteration
*/
type F = (x: number) => number;

function compose(functions: F[]): F {
	return function(x) {
        let res = x
        for (let i = functions.length-1; i >= 0 ; i--) {
            res = functions[i](res)
        }
        return res
    }
};

/*
    2nd: recursion
*/
function compose(functions: F[]): F {
    if (functions.length === 0) {
        return function (x) { return x }
    }
    const first = functions[0]
    const rest = compose(functions.slice(1))
	return function(x) {
        return first(rest(x))
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */