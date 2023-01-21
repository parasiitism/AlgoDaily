/*
    Binary Indexed Tree

    Time of init()      O(N)
    Time of gather()    O(maxRow)
    Time of scatter()   O(logM + maxRow)
    Space               O(N)

    Runtime 10341 ms beats 20%
*/
class BookMyShow {
    constructor(n, m) {
        this.n = n;
        this.m = m;
        this.used = Array(n).fill(0),
        this.BIT = new BinaryIndexedTree(n);
        for (let i = 0; i < n; i++) {
            this.BIT.update(i, m);
        }
    }

    gather(k, maxRow) {
        for (let i = 0; i <= maxRow; i++) {
            let seats = this.m - this.used[i];
            if (seats >= k) {
                let first = this.used[i];
                this.used[i] += k;
                this.BIT.update(i, -k);
                return [i, first];
            }
        }
        return [];
    }

    scatter(k, maxRow) {
        const total = this.BIT.getSum(maxRow); // use fenwick to query [0, maxRow] range sum
        if (total < k) {
            return false;
        }
        for (let i = 0; i <= maxRow; i++) {
            let seats = this.m - this.used[i];
            if (seats >= k) {
                this.used[i] += k;
                this.BIT.update(i, -k);
                k = 0;
            } else {
                k -= seats;
                this.BIT.update(i, -seats);
                this.used[i] += seats;
            }
        }
        return true;
    }
}

class BinaryIndexedTree {
    constructor(n) {
        this.fenwickTree = Array(n+1).fill(0);
    }
    update(i, val) {
        let k = i + 1
        while (k < this.fenwickTree.length) {
            this.fenwickTree[k] += val
            k += k & -k
        }
    }
    getSum(i) {
        let total = 0
        let k = i + 1
        while (k > 0) {
            total += this.fenwickTree[k]
            k -= k & -k
        }
        return total
    }
}