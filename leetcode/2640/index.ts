/*
    prefix sum

    Time    O(N)
    Space   O(N)
*/
function findPrefixScore(nums: number[]): number[] {
    let res: Array<number> = []
    let cur_max: number = 0
    let pfs: number = 0
    for (let x of nums) {
        cur_max = Math.max(cur_max, x)
        pfs += cur_max + x
        res.push(pfs)
    }
    return res
};