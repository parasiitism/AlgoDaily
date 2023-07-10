var invalidTransactions = function(transactions) {
    const ht = {} // {time: {user: {city}}}
    for (let T of transactions) {
        const [user, _t, _amount, city] = T.split(',')
        const t = parseInt(_t)
        const amount = parseInt(_amount)
        // if (amount > 1000) {
        //     continue
        // }
        if (t in ht === false) {
            ht[t] = {}
        }
        if (user in ht[t] === false) {
            ht[t][user] = new Set()
        }
        ht[t][user].add(city)
    }
    const res = []
    for (let T of transactions) {
        const [user, _t, _amount, city] = T.split(',')
        const t = parseInt(_t)
        const amount = parseInt(_amount)
        if (amount > 1000) {
            res.push(T)
            continue
        }
        for (let i = t-60; i <= t+60; i++) {
            if (i in ht === false) {
                continue
            }
            if (user in ht[i] === false) {
                continue
            }
            if (ht[i][user].size > 1 || ht[i][user].keys().next().value != city) {
                res.push(T)
                break
            }
        }
    }
    return res
};