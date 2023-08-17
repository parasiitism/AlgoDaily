/**
 * @param {number[]} digits
 * @return {number[]}
 * 
 *  1st approach: carry
    - like adding 2 big numbers
    
    Time    O(n)
    Space   O(1)
    52 ms, faster than 82.83%
 */
var plusOne = function (digits) {
	let carry = 1;
	const n = digits.length;
	for (let i = n - 1; i >= 0; i--) {
		const temp = digits[i] + carry;
		digits[i] = temp % 10;
		carry = Math.floor(temp / 10);
	}
	if (carry > 0) {
		digits = [carry, ...digits];
	}
	return digits;
};

/*
    2nd: input immutable, use an extra array for the result

    Time    O(N)
    Space   O(N) the result
    52 ms, faster than 82.83%
*/
var plusOne = function(digits) {
    const n = digits.length
    const res = []
    let carry = 1
    for (let i = n-1; i >= 0; i--) {
        const x = digits[i]
        const d = (x + carry) % 10
        carry = Math.floor((x + carry) / 10)
        res.push(d)
    }
    if (carry > 0) {
        res.push(carry)
    }
    res.reverse()
    return res
};