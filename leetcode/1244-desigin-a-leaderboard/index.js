/*
    1st: binary search + hashtable

    - maintain an array to store the ids sorted by scores
    - a hashtable to store the relation for every {id: score}

    Time of addScore()      O(k), it can be O(logN) depends on language becos of array.insert()
    Time of top()           O(k)
    Time of reset()         O(N) binary search + linear search
    Space                   O(2N)
    96 ms, faster than 92.31%
*/
var Leaderboard = function() {
    this.arr = []   // ids sort by scores
    this.ht = {}    // {id1: score1, id2: score2}
};
Leaderboard.prototype.addScore = function(playerId, score) {
    let newScore = 0
    if (playerId in this.ht) {
        newScore = this.ht[playerId] + score
        this.ht[playerId] = newScore
        // remove
        const i = this.arr.indexOf(playerId)
        this.arr.splice(i, 1)
    } else {
        this.ht[playerId] = score
        newScore = score
    }
    // add
    const j = upperBsearch(this.arr, this.ht, newScore)
    this.arr.splice(j, 0, playerId)
};
Leaderboard.prototype.top = function(K) {
    let res = 0
    let count = 0
    for (let i = this.arr.length-1; i >= 0; i--) {
        const pId = this.arr[i]
        res += this.ht[pId]
        count += 1
        if (count === K) { break }
    }
    return res
};
Leaderboard.prototype.reset = function(playerId) {
    const i = this.arr.indexOf(playerId)
    this.arr.splice(i, 1)
    delete this.ht[playerId]
};
const upperBsearch = (arr, ht, target) => {
	let left = 0;
	let right = arr.length;
	while (left < right) {
		const mid = Math.floor((left + right) / 2);
        const pId = arr[mid]
		if (target >= ht[pId]) {
			left = mid + 1;
		} else {
			right = mid;
		}
	}
	return left;
};

/*
    2nd: binary search + hashtable

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