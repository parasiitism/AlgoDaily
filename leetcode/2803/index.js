/*
    JS generator

    Time    O(N)
    Space   O(1)
*/
function* factorial(n) {
    if (n == 0) {
        yield 1
    }
    let res = 1
    for(let i = 1; i <= n; i++) {
        res *= i
        yield res
    }
};