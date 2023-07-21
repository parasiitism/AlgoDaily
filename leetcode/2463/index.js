/*
    brute-force
    - the return of DFS is the cost of fixing robot[0]...robot[r] at factory[f] with number of fixes
    
    TLE: 5 / 40 testcases passed
*/
var minimumTotalDistance = function(robot, factory) {
    const R = robot.length
    const F = factory.length

    robot.sort((a, b) => a - b)
    factory.sort((a, b) => a[0] - b[0])

    const dfs = (r, f, fixed) => {
        if (r >= R) {
            return 0
        }
        if (f >= F) {
            return 2**32
        }

        const skipInThisFactory = dfs(r, f+1, 0)
        let fixInThisFactory = 2**32
        if (factory[f][1] > fixed) {
            fixInThisFactory = dfs(r+1, f, fixed+1) + Math.abs(robot[r] - factory[f][0])
        }
        return Math.min(skipInThisFactory, fixInThisFactory)
    }

    return dfs(0, 0, 0)
};

/*
    2nd: optimize 1st with a hashtable

    Time    O(RFC) R: robot, F: factory, C: avery capacity of every factory
    Space   O(RFC) the hashtable
*/
var minimumTotalDistance = function(robot, factory) {
    const R = robot.length
    const F = factory.length

    robot.sort((a, b) => a - b)
    factory.sort((a, b) => a[0] - b[0])

    const cache = {}

    const dfs = (r, f, fixed) => {
        if (r >= R) {
            return 0
        }
        if (f >= F) {
            return 2**40
        }
        const key = `${r},${f},${fixed}`
        if (key in cache) {
            return cache[key]
        }

        const skipInThisFactory = dfs(r, f+1, 0)
        let fixInThisFactory = 2**40
        if (factory[f][1] > fixed) {
            fixInThisFactory = dfs(r+1, f, fixed+1) + Math.abs(robot[r] - factory[f][0])
        }
        cache[key] = Math.min(skipInThisFactory, fixInThisFactory)
        return cache[key]
    }

    return dfs(0, 0, 0)
};