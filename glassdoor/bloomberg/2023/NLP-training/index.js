/*
    Questions: Given some sentences, do 3 tasks

    input =[
        ["I","am","Sam"],
        ["I","am","Bob"],
        ["I","like","eggs"]
    ]

    1. For every word, calculate the next word which will most-possibly appear

    2. For every word, print all the next words will appear with given frequency

    3. Write a function which accept a word as an input, print the most-possibly appear (similar to 1st)

    4. Followup: if the system keep giving you the sentenses?

    ref: https://www.1point3acres.com/bbs/thread-1002755-1-1.html

------------------- questions to ask -------------------------

    1. two or more words have the same frequency?
    2. uppercase, lowercase?

*/
class NLPTraining {
    constructor(sentences) {
        this.freqs = {} // neseted map { cur: { next: int } }
        this.cacheMostFreq = {} // { word: [next word, int] }
        for (let s of sentences) {
            this.addSentence(s)
        }
    }

    addSentence(S) {
        const n = S.length
        for (let i = 0; i < n-1; i++) {
            const cur = S[i]
            const next = S[i+1]
            if (cur in this.freqs === false) {
                this.freqs[cur] = {}
            }
            if (next in this.freqs[cur] === false) {
                this.freqs[cur][next] = 0
            }
            this.freqs[cur][next] += 1

            // update cache
            if (cur in this.cacheMostFreq === false) {
                this.cacheMostFreq[cur] = [null, 0]
            }
            if (this.freqs[cur][next] > this.cacheMostFreq[cur][1]) {
                this.cacheMostFreq[cur] = [next, this.freqs[cur][next]]  
            }
        }
    }

    printAllPossibilities() {
        console.log(this.freqs)
    }

    getTheMostPossibleNextWord(word) {
        if (word in this.cacheMostFreq === false) {
            return null
        }
        return this.cacheMostFreq[word][0]
    }
}

const sentences =[
    ["I","am","Sam"],
    ["I","am","Bob"],
    ["I","like","eggs"]
]

const nlp = new NLPTraining(sentences)
nlp.printAllPossibilities()

console.log(nlp.getTheMostPossibleNextWord('I'))

nlp.addSentence(["I", "like", "eggs"])
nlp.addSentence(["I", "like", "eggs"])

console.log(nlp.getTheMostPossibleNextWord('I'))