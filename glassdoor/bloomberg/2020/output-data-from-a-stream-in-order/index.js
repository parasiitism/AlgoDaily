/*
    - https://leetcode.com/discuss/interview-question/314733/bloomberg-output-data-from-a-stream-in-order
    - https://leetcode.com/problems/design-an-ordered-stream/description/

    There is a continous stream of data in the form of:
    Input: (1, "abcd"), (2, "efgh"), (4, "mnop"), (5, "qrst"), (3, "ijkl")

    Write a program to output the data from the stream in realtime in order, so 1,2,3,4,5..
    You cannot queue up the incoming data from the stream.
    So for example if the first incoming bit of data is (1, "abcd"), and the second is (4, "mnop"), you cannot output (4, "mnop") until you get 2, 3.


    Stream input

    questions:
    - no duplicate IDs?
    - no duplicate strings?
    - if we reach to z, should we rotate back to a?
    - can i assume, the s is in order? e.g. (1, "abcd") but bot (1, "abdc") ?
*/

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
