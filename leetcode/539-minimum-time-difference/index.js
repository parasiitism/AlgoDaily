/*
    1st: math + sort
    - transform the time to hour * 60 + minute

    Time    O(NlogN)
    Space   O(N)
*/
var findMinDifference = function(timePoints) {
    const times = []
    for (let t of timePoints) {
        const x = s2int(t)
        times.push(x)
        times.push(x+1440)
    }
    times.sort((a, b) => a - b)
    let res = 24*60
    for (let i = 1; i < times.length; i++) {
        const diff = times[i] - times[i-1]
        res = Math.min(res, diff)
    }
    return res
};

const s2int = s => {
    const [hh, mm] = s.split(':')
    const h = Number(hh)
    const m = Number(mm)
    return h*60+m
}