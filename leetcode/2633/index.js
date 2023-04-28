/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function(object) {
    if (object === null) {
        return 'null'
    }
    if (typeof object === 'boolean') {
        return object ? 'true' : 'false' 
    }
    if (typeof object === 'number') {
        return object.toString()
    }
    if (Array.isArray(object)) {
        const list = []
        for (let x of object) {
            list.push(jsonStringify(x))
        }
        return '[' + list.join(',') + ']'
    }
    if (typeof object === 'object') {
        const list = []
        for (let key of Object.keys(object)) {
            const s = jsonStringify(key) + ":" + jsonStringify(object[key])
            list.push(s)
        }
        return '{' + list.join(',') + '}'
    }
    // only 'string' type is remaining
    return '"'+object+'"'
};