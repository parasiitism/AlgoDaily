class OrderedStream {
    constructor() {
        this.ptr = 1
        this.ht = {}
    }
    insert(idKey, value) {
        this.ht[idKey] = value
        const res = []
        while (this.ptr in this.ht) {
            res.push(this.ht[this.ptr])
            this.ptr += 1
        }
        return res
    }
}