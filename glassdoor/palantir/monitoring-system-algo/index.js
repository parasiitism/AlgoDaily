/*
    Questions
    - How long do the getMetrics() and and putData() take?
        uncertain - can be a few ms or a few sec
    - What if they fail? do we retry or just discard?
        retry n times, give up before 30s
    - Will there be API to cancel the requests if one takes too long?
        if http, AbortController
        if not, we need to know

*/
const retry = async (fn, params=[], atMost=3, expoBase=3) => {
	let times = 0
    const execute = async () => {
        try {
            const res = await fn(...params)
            console.log(res, Date.now())
            return res
        } catch(error) {
            times += 1
            if (times == atMost) {
                throw error
            }
            const delay = expoBase ** times
            await new Promise((resolve) => setTimeout(() => resolve(), delay))
            return await execute()
        }
    }
    return await execute()
}

const retry2 = async (fn, params=[], atMost=3, expoBase=3) => {
    let times = 0
    while (count < maxCount) {
        try {
            const res = await fn(...params)
            console.log(res, Date.now())
            return res
        } catch(error) {
            times += 1
            if (times == atMost) {
                throw error
            }
            const delay = expoBase ** times
            await new Promise((resolve) => setTimeout(() => resolve(), delay))
        }
    }
}

// const executeAll = async () => {
//     const nPromises = [
//         () => new Promise(resolve => setTimeout(() => resolve(1), 3000)),
//         () => new Promise(resolve => setTimeout(() => resolve(2), 3000)),
//         () => new Promise(resolve => setTimeout(() => resolve(3), 3000)),
//     ]
//     const tasks = nPromises.map(p => retry(p))
//     const res =  await Promise.all(tasks)
//     console.log(res)
//     return res
// }
// executeAll()

/*
    Here!
*/

const getMetrics = host => {
    console.log(`getMetrics ${host}`)
    return new Promise(resolve => setTimeout(() => resolve(`host: ${host} { cpu: 50% }`), 3000))
}

const putData = data => {
    console.log(`putData ${data}`)
    return new Promise(resolve => setTimeout(() => resolve(`data: ${data}`), 1000))
}

const startMonitoring = () => {
    const hosts = ['AAA', 'BBB', 'CCC', 'DDD', 'EEE']
    setInterval(async () => {
        const nPromises = []
        for (let host of hosts) {
            const task = retry(getMetrics, [host], 1).then((metrics) => retry(putData, [metrics], 1))
            nPromises.push(task)
        }
        const res = await Promise.allSettled(nPromises)
        // we can count the success rate by using the array item status: 'fulfilled' | 'rejected'
    }, 10000);
}
startMonitoring()