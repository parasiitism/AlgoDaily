/*
    JS
    
    Time    O(N)
    Space   O(N)
*/
var createObject = function(keysArr, valuesArr) {
    const res = {}
    for (let i = 0; i < keysArr.length; i++) {
        const key = keysArr[i]
        const val = valuesArr[i]
        if (key in res == false) {
            res[key] = val
        }
    }
    return res
};