/*
    You work in an electronic exchange. Throughout the day, you receive ticks (trading data) which consists of product name and its traded volume of stocks. Eg: {name: vodafone, volume: 20}. What data structure will you maintain if:

    - You have to tell top k products traded by volume at end of day.
    - You have to tell top k products traded by volume throughout the day.

    stream of input of
    {EURUSD, 100}
    {CHFEUR, 200}
    {EURUSD, 100}‍‌‌‍‌‍‌‍‍‌‌‌‍‌‌‌‍‌‌
    return the top k total amount
*/

/*
    leetcode1244, there are a few solutions. 
    The most optimal one is to use a BST, then do a inorder travesal to get Top(K)
*/
class BSTNode {
    constructor(volume, ticker) {
        this.volume = volume
        this.tickers = new Set([ticker])
        this.left = null
        this.right = null
    }
}
class BST {
    constructor() {
        this.root = null
    }
    insert(ticker, volume) {
        if (this.root === null) {
            const node = new BSTNode(volume, ticker)
            this.root = node
            return
        }
        let cur = this.root
        while (cur !== null) {
            if (volume < cur.volume) {
                if (!cur.left) {
                    cur.left = new BSTNode(volume, ticker)
                    return
                }
                cur = cur.left
            } else if (volume > cur.volume) {
                if (!cur.right) {
                    cur.right = new BSTNode(volume, ticker)
                    return
                }
                cur = cur.right
            } else {
                break
            }
        }
        cur.tickers.add(ticker)
    }
    delete(ticker, volume) {
        // we can just delete the key in target_node hashset, 
        // instead of deleting a BST node
        let cur = this.root
        while (cur !== null) {
            if (volume < cur.volume) {
                cur = cur.left
            } else if (volume > cur.volume) {
                cur = cur.right
            } else {
                break
            }
        }
        cur.tickers.delete(ticker)
    }
    topK(k) {
        let total = 0
        const inorder = node => {
            if (node === null) {
                return
            }
            inorder(node.right)
            const toConsider = Math.min(node.tickers.size, k)
            total += node.volume * toConsider
            k -= toConsider
            inorder(node.left)
        }
        inorder(this.root)

        return total
    }
    _rebalance() {
        const A = []
        const inorder = node => {
            if (node === null) {
                return
            }
            inorder(node.left)
            if (node.tickers.size > 0) {
                A.push(node)
            }
            inorder(node.right)
        }
        inorder(this.root)

        const partition = (L, R) => {
            if (L > R) {
                return null
            }
            const half = Math.floor((L+R)/2)
            const oldNode = A[half]
            const node = new BSTNode(oldNode.volume, oldNode.tickers)
            node.left = partition(L, half-1)
            node.right = partition(half+1, R)
            return node
        }

        this.root = partition(0, A.length-1)
    }
}

class Exchange {
    constructor() {
        this.ht = {}
        this.bst = new BST()
    }
    execute(ticker, volume) {
        if (ticker in this.ht === false) {
            this.ht[ticker] = volume
            this.bst.insert(ticker, volume)
        } else {
            const oldVolume = this.ht[ticker]
            const newVolume = oldVolume + volume
            this.ht[ticker] = newVolume

            this.bst.delete(ticker, oldVolume)
            this.bst.insert(ticker, newVolume)
        }
    }
    topK(k) {
        return this.bst.topK(k)
    }
}

const exchange = new Exchange()
exchange.execute('HKDJPN', 300)
exchange.execute('EURUSD', 100)
exchange.execute('CHFEUR', 200)
exchange.execute('HKDGBP', 400)
console.log(exchange.topK(3))
/*
    result = 400 + 300 + 200 = 900

    because
    400: HKDGBP
    300: HKDJPN
    200: CHFEUR
    100: EURUSD
*/
exchange.execute('EURUSD', 1000)
exchange.execute('CHFEUR', 999)
console.log(exchange.topK(3))
/*
    result = 1199 + 1100 + 400 = 2699
    
    because
    1199: CHFEUR
    1100: EURUSD
    400: HKDGBP
    300: HKDJPN
*/
exchange.execute('JPNUSD', 1100)
console.log(exchange.topK(3))
/*
    result = 1199 + 1100 + 1100 = 3399
    
    because
    1199: CHFEUR
    1100: EURUSD
    1100: JPNUSD
    400: HKDGBP
    300: HKDJPN
*/
exchange.execute('EURUSD', 1000)
console.log(exchange.topK(3))
/*
    result = 2100 + 1199 + 1100 = 4399
    
    because
    2100: EURUSD
    1199: CHFEUR
    1100: JPNUSD
    400: HKDGBP
    300: HKDJPN
*/