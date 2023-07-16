var join = function(arr1, arr2) {
    const seen = {}
    const res = []
    for (let i = 0; i < arr1.length; i++) {
        const obj = arr1[i]
        res.push({...obj})
        seen[obj.id] = i
    }

    for (let obj of arr2) {
        const id = obj.id
        if (id in seen) {
            const i = seen[id]
            const orginal = res[i]
            const _obj = {...orginal}
            for (const k in obj) {
                _obj[k] = obj[k]
            }
            
            res[i] = _obj

        } else {
            res.push(obj)
        }
    }
    res.sort((a, b) => a.id - b.id)
    return res
};