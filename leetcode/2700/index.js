/*
    1st: JS

    Time    O(N)
    Space   O(N)
*/

/**
 * @param {object} obj1
 * @param {object} obj2
 * @return {object}
 */
function objDiff(obj1, obj2) {
    const diffs = {}
    for (let key in obj1) {
        if (key in obj2) {
            const val1 = obj1[key]
            const val2 = obj2[key]

            if (val1 instanceof Object === false || val2 instanceof Object === false){
                if (val1 !== val2){
                    diffs[key] = [val1,val2];
                }
            } else if (Array.isArray(val1) !== Array.isArray(val2)) {
                diffs[key] = [val1, val2];
            } else {
                const sub_diff = objDiff(val1, val2);
                const len = Object.keys(sub_diff).length;
                if (len === 0)
                    continue;
                diffs[key] = sub_diff;
            }
        }
    }
    return diffs
};