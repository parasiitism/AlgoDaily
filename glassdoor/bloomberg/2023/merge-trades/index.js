/*
    Exmaple1:

        Trades
        [ (“TSLA US Equity”, 500), (“TSLA US Equity”, 600), (“VOD LN Equity”, 1000), (“TSLA UW Equity”, 250)]

        Equivalences
        [ (“TSLA US Equity”, “TSLA UB Equity”), (“TSLA UB Equity”, “TSLA UW Equity”), (“VOD LN Equity”, “VOD IN Equity”)]

        Here we have to consider TSLA US Equity, TSLA UB Equity, TSLA UB Equity, TSLA UW Equity as one company and count trade values from Trades input.

        Output
        [ ("TSLA US Equity", 1350), ("VOD LN Equity", 1000) ]

    Example2:

        Trades
        [ (“TSLA US Equity”, 500), ("TSLA UQ Equity", 100)]

        Equivalences
        [ ("TSLA US Equity", "TSLA UB Equity"), ("TSLA UQ Equity", "TSLA UW Equity"), ("TSLA UB Equity", "TSLA UQ Equity") ]

        Output
        [ (“TSLA US Equity”, 600)]

    ref:
    - https://leetcode.com/discuss/interview-question/2798094/Bloomberg-onsite-interview-experience

    ===== approach =====

    Simular to union-find
    - create a graph first, { child: parent }
    - loop for the nodes, find its root parent and store it in a hashtable
    - loop over the trades, increment the volume

    Time    O(E + N^2 or NlogN + N) NlogN because if the tree is balanced, the height of the tree is the lookup time
    Space   O(N)
*/
const mergeTrades = (trades, equivalences) => {
    
    const G = {} // { child: parent }
    for (let [u, v] of equivalences) {
        if (u in G === false) { G[u] = u }
        if (v in G === false) { G[v] = v }
        G[v] = u
    }

    const roots = {}
    for (let node in G) {
        let cur = node
        while (G[cur] != cur) {
            cur = G[cur]
        }
        roots[node] = cur
    }

    const m = {}
    for (let [ticker, volume] of trades) {
        const r = roots[ticker]
        if (r in m == false) {
            m[r] = 0
        }
        m[r] += volume
    }

    const res = []
    for (let key in m) {
        res.push([key, m[key]])
    }
    return res
}

let a = [
    ['TSLA US Equity', 500], ['TSLA US Equity', 600], ['VOD LN Equity', 1000], ['TSLA UW Equity', 250]
]
let b = [
    ['TSLA US Equity', 'TSLA UB Equity'], ['TSLA UB Equity', 'TSLA UW Equity'], ['VOD LN Equity', 'VOD IN Equity']
]
console.log(mergeTrades(a, b))

a = [
    ['TSLA US Equity', 500], ['TSLA UQ Equity', 100]
]
b = [
    ['TSLA US Equity', 'TSLA UB Equity'], ['TSLA UQ Equity', 'TSLA UW Equity'], ['TSLA UB Equity', "TSLA UQ Equity"]
]
console.log(mergeTrades(a, b))