/*
    1st: binary search + hashtable

    Time of addScore()      O(logN + N) binary search + remove
    Time of top()           O(K)
    Time of reset()         O(logN + N) binary search + remove
    Space                   O(2N)
    96 ms, faster than 92.31%
*/
class Leaderboard {
    constructor() {
        this.sortedList = []    // scores
        this.playerScore = {}   // playerId: score
    }
    addScore(playerId, score) {
        if (playerId in this.playerScore === false) {
            this.playerScore[playerId] = score
            const i = this.lowerBsearch(score)
            this.sortedList.splice(i, 0, score) // insert
        } else {
            const oldScore = this.playerScore[playerId]
            const i = this.lowerBsearch(oldScore)
            this.sortedList.splice(i, 1) // delete
            
            const newScore = oldScore + score
            this.playerScore[playerId] = newScore
            const j = this.lowerBsearch(newScore)
            this.sortedList.splice(j, 0, newScore) // insert
        }
    }
    top(k) {
        const n = this.sortedList.length
        let total = 0
        const bound = Math.max(0, n-k)
        for (let i = n-1; i >= bound; i--) {
            total += this.sortedList[i]
        }
        return total
    }
    reset(playerId) {
        if (playerId in this.playerScore === false) {
            return
        }
        const oldScore = this.playerScore[playerId]
        const i = this.lowerBsearch(oldScore)
        this.sortedList.splice(i, 1) // delete
        
        delete this.playerScore[playerId]
    }
    lowerBsearch(target) {
        let left = 0
        let right = this.sortedList.length - 1
        let res = this.sortedList.length
        while (left <= right) {
            const mid = Math.floor((left + right) / 2)
            if (target <= this.sortedList[mid]) {
                res = mid
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
        return res
    }
}

/*
    2nd: BST
    - for interview purpose
        - don't rebalance the tree
        - don't implement BST.deleteNode(), just search the node and delete the user from hashset instead
    - worst time complexity of insert() and deleted() is O(N), but O(logN) on average
    - time of topk() is still O(K)

    Time of addScore()      O(logN)
    Time of top()           O(logN)
    Time of reset()         O(K)
    Space   O(N)
    149ms beats 20%
*/
class Leaderboard {
    constructor() {
        this.ht = {} // { player: score }
        this.bst = new BST()
    }
    addScore(playerId, score) {
        if (playerId in this.ht === false) {
            this.ht[playerId] = score
            this.bst.insert(playerId, score)
        } else {
            const oldScore = this.ht[playerId]
            const newScore = oldScore + score
            this.ht[playerId] += score

            this.bst.delete(playerId, oldScore)
            this.bst.insert(playerId, newScore)
        }
    }
    top(k) {
        return this.bst.topK(k)
    }
    reset(playerId) {
        if (playerId in this.ht === false) {
            return
        }
        const oldScore = this.ht[playerId]
        this.bst.delete(playerId, oldScore)
        delete this.ht[playerId]
    }
}

class BSTNode {
    constructor(score, player) {
        this.score = score
        this.players = new Set([player])
        this.left = null
        this.right = null
    }
}

class BST {
    constructor() {
        this.root = null
    }
    insert(player, score) {
        if (this.root === null) {
            const node = new BSTNode(score, player)
            this.root = node
            return
        }
        let cur = this.root
        while (cur !== null) {
            if (score < cur.score) {
                if (!cur.left) {
                    cur.left = new BSTNode(score, player)
                    return
                }
                cur = cur.left
            } else if (score > cur.score) {
                if (!cur.right) {
                    cur.right = new BSTNode(score, player)
                    return
                }
                cur = cur.right
            } else {
                break
            }
        }
        cur.players.add(player)
    }
    delete(player, score) {
        // we can just delete the key in target-node hashset, instead of deleting a BST node
        let cur = this.root
        while (cur !== null) {
            if (score < cur.score) {
                cur = cur.left
            } else if (score > cur.score) {
                cur = cur.right
            } else {
                break
            }
        }
        cur.players.delete(player)
    }
    topK(k) {
        console.log(this.root)
        let total = 0
        const inorder = node => {
            if (node === null) {
                return
            }
            inorder(node.right)
            const toConsider = Math.min(node.players.size, k)
            total += node.score * toConsider
            k -= toConsider
            inorder(node.left)
        }
        inorder(this.root)

        return total
    }
}

/*
    3rd: optimization with rebalancing
*/
class Leaderboard {
    constructor() {
        this.ht = {} // { player: score }
        this.bst = new BST()
    }
    addScore(playerId, score) {
        if (playerId in this.ht === false) {
            this.ht[playerId] = score
            this.bst.insert(playerId, score)
        } else {
            const oldScore = this.ht[playerId]
            const newScore = oldScore + score
            this.ht[playerId] += score

            this.bst.delete(playerId, oldScore)
            this.bst.insert(playerId, newScore)
        }
    }
    top(k) {
        return this.bst.topK(k)
    }
    reset(playerId) {
        if (playerId in this.ht === false) {
            return
        }
        const oldScore = this.ht[playerId]
        this.bst.delete(playerId, oldScore)
        delete this.ht[playerId]
    }
}

class BSTNode {
    constructor(score, players=[]) {
        this.score = score
        this.players = new Set(players)
        this.left = null
        this.right = null
    }
}

class BST {
    constructor() {
        this.root = null
        this.deleteCount = 0
    }
    insert(player, score) {
        if (this.root === null) {
            this.root = new BSTNode(score, [player])
            return
        }
        let cur = this.root
        while (cur !== null) {
            if (score < cur.score) {
                if (!cur.left) {
                    cur.left = new BSTNode(score, [player])
                    return
                }
                cur = cur.left
            } else if (score > cur.score) {
                if (!cur.right) {
                    cur.right = new BSTNode(score, [player])
                    return
                }
                cur = cur.right
            } else {
                break
            }
        }
        cur.players.add(player)
    }
    delete(player, score) {
        let cur = this.root
        while (cur !== null) {
            if (score < cur.score) {
                cur = cur.left
            } else if (score > cur.score) {
                cur = cur.right
            } else {
                break
            }
        }
        cur.players.delete(player)
        this.deleteCount += 1
        if (this.deleteCount > 30) { // just a random number for now
            this._rebalance()
            this.deleteCount = 0
        }
    }
    _rebalance() {
        const A = []
        const inorder = node => {
            if (node === null) {
                return
            }
            inorder(node.left)
            if (node.players.size > 0) {
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
            const node = new BSTNode(oldNode.score, oldNode.players)
            node.left = partition(L, half-1)
            node.right = partition(half+1, R)
            return node
        }

        this.root = partition(0, A.length-1)
    }
    topK(k) {
        let total = 0
        const inorder = node => {
            if (node === null) {
                return
            }
            inorder(node.right)
            const toConsider = Math.min(node.players.size, k)
            total += node.score * toConsider
            k -= toConsider
            inorder(node.left)
        }
        inorder(this.root)

        return total
    }
}