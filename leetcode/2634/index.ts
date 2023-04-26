function filter(arr: number[], fn: (n: number, i: number) => any): number[] {
    const res = []
    for (let i = 0; i < arr.length; i++) {
        const x = arr[i]
        const b = fn(x, i)
        if (b) {
            res.push(x)
        }
    }
    return res
};