/*
    https://leetcode.com/discuss/interview-question/312500/eBay-phone-screen-Currency-exchange-rate

    We are given a list of list, for a currency exchnage application.
    [["USD","CAD",1.5] , ["CAD", "INR", 50] ,["INR", "BAD", 1.54] ],

    How do you calculate one currency to another currency, that is find the exchange rate? when a method is given such as exchnageValue(currency c1, currency c2)

    followups:
    1. make it a system, the currency can be added/changed in real time
    2. return the best rate for every query
*/
class CurrencyExchange {
    constructor() {
        this.G = {}
    }
    upsertRate(a, b, rate) {
        if (a in this.G === false) { this.G[a] = {} }
        if (b in this.G === false) { this.G[b] = {} }
        
        this.G[a][b] = rate
        this.G[b][a] = 1.0/rate
    }
    queryRate(src, dest) {
        if (src in this.G === false || dest in this.G === false) {
            return -1
        }
        const seen = new Set()
        const q = [[src, 1.0]]
        while (q.length > 0) {
            const [node, ratio] = q.shift()
            if (node == dest) {
                return ratio
            }
            if (node in this.G == false) {
                continue
            }
            if (seen.has(node)) {
                continue
            }
            seen.add(node)
            for (let child in this.G[node]) {
                const toMultiply = this.G[node][child]
                q.push([child, ratio * toMultiply])
            }
        }
        return -1
    }
}

const s = new CurrencyExchange()

s.upsertRate('USD', 'HKD', 8)
s.upsertRate('HKD', 'JPY', 13)
console.log(s.queryRate('USD', 'JPY')) // 104

s.upsertRate('USD', 'HKD', 7.75)
s.upsertRate('HKD', 'JPY', 13)
console.log(s.queryRate('USD', 'JPY')) // 100.75

console.log(s.queryRate('USD', 'CAD')) // -1