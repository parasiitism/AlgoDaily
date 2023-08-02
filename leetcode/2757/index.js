/*
    For JS generator, we receive the param of the next() by "yield" result
*/
var cycleGenerator = function* (arr, startIndex) {
    let i = startIndex
    while (true) {
        const jump = yield arr[i]
        i = (i + arr.length + jump % arr.length) % arr.length
    }
};