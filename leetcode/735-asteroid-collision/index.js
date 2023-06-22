/*
    1st approach: stack
    - similar to lc402
    - if positive, just put into stack
    - if negative:
      1. - pop the stack if abs(num) is larger than the top item in the stack
         - if the stack becomes empty, append the num into the res array
      2. pop the stack if abs(num) == stack[-1], skip appending

    Time    O(n)
    Space   O(n)
    88 ms, faster than 63.04%
*/
var asteroidCollision = function (asteroids) {
	const S = []
    for (let i = 0; i < asteroids.length; i++) {
        const x = asteroids[i]
        if (x >= 0) {
            S.push(x)
        } else {
            while (S.length > 0 && S[S.length-1] > 0 && S[S.length-1] < -x ) {
                S.pop()
            }
            if (S.length > 0 && S[S.length-1] == -x) {
                S.pop()
            } else if (S.length === 0 || S[S.length-1] < 0) {
                S.push(x)
            }
        }
    }
    return S
};
