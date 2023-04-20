async function sleep(millis) {
    return new Promise((resolve, _reject) => setTimeout(() => resolve(), millis))
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */