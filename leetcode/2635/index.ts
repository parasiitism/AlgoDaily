function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    const res: Array<number> = []
    for (let i = 0; i < arr.length; i++) {
        const new_x = fn(arr[i], i)
        res.push(new_x)
    }
    return res
};