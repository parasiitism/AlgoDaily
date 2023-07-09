/*
    3rd approach: learned from others
	- calculate the products from the front & from the back
		e.g.
							2		3 		4 		5
						->	1		1*2		2*3		2*3*4
							3*4*5	4*5		5*1			1		<-
							-----------------------
			result = 60		20		30			12
	- the cruz of the question is to learn this approach, it is slow but it doesn't matter
	Time	O(3n)
	Space	O(2n)
	76 ms, faster than 89.52%
	8ay2019
*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
	const n = nums.length
    const forward = Array(n).fill(1)
    const backward = Array(n).fill(1)
    let cur = 1
    for (let i = 0; i < n; i++) {
        forward[i] = cur
        cur *= nums[i]
    }
    cur = 1
    for (let i = n-1; i>= 0; i--) {
        backward[i] = cur
        cur *= nums[i]
    }
    const res = Array(n).fill(1)
    for (let i = 0; i < n; i++) {
        res[i] = forward[i] * backward[i]
    }
    return res
};

/*
    4th approach: learned from others
    - similar to lc236, 1644, 1650, 1676
	- calculate the products from the front & from the back
		e.g.
							2		3 		4 		5
						->	1		1*2		2*3		2*3*4
							3*4*5	4*5		5*1			1		<-
							-----------------------
			        result = 60		20		30			12
	- the cruz of the question is to learn this approach, it is slow but it doesn't matter
	Time	O(2n)
	Space	O(1) exlcuding the result
	208 ms, faster than 28.59%
*/
var productExceptSelf = function(A) {
    const n = A.length
    const res = Array(n).fill(1)
    for (let i = 1; i < n; i++) {
        res[i] = res[i-1] * A[i-1]
    }
    let cur = 1
    for (let i = n-1; i >= 0; i--) {
        res[i] *= cur
        cur *= A[i]
    }
    return res
};
