class PhoneDirectory {
    constructor(maxNum) {
        this.availables = new Set()
        for (let i = 0; i < maxNum; i++) {
            this.availables.add(i)
        }
    }
    get() {
        if (this.availables.size == 0) {
            return -1
        }
        const first = this.availables.keys().next().value
        this.availables.delete(first)
        return first
    }
    check(number) {
        return this.availables.has(number)
    }
    release(number) {
        if (this.availables.has(number)) {
            return
        }
        this.availables.add(number)
    }
}