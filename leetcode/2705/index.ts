
type Obj = Record<any, any>;

function compactObject(obj: Obj): Obj {
    if (Array.isArray(obj)) {
        const res = []
        for (let x of obj) {
            if (x instanceof Object) {
                res.push(compactObject(x))
            } else if (Boolean(x) === true){
                res.push(x)
            }
        }
        return res
    }
    const res = {}
    for (let k in obj) {
        const v = obj[k]
        if (v instanceof Object) {
            res[k] = compactObject(v)
        } else if (Boolean(v) === true){
            res[k] = v
        }
    }
    return res
};