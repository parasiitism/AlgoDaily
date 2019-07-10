/*
    examples:

    calvin is handsome => c4n is h6e
    calvin is-handsome => c4n is-h6e
    calvin is--handsome => c4n is--h6e
    calvin-  -is handsome => c4n-  -is h6e
     calvin is--handsome =>  c4n is--h6e
*/

function f(s) {

    const delimiters = []
    let temp = ''
    for (let i = 0; i < s.length; i++) {
        if (i > 0 && (s[i - 1] == ' ' || s[i - 1] == '-') && (s[i] == ' ' || s[i] == '-')) {
            temp += s[i]
        } else if (s[i] == ' ' || s[i] == '-') {
            temp = s[i]
        } else if (temp.length > 0) {
            delimiters.push(temp)
            temp = ''
        }
    }
    if (temp.length > 0) {
        delimiters.push(temp)
    }

    const words = s.split(/[ -]+/)
    let res = ''
    for (let i = 0; i < words.length; i++) {
        if (i < delimiters.length) {
            res += shorten(words[i]) + delimiters[i]
        } else {
            res += shorten(words[i])
        }

    }
    return res
}

function shorten(word) {
    if (word.length <= 2) {
        return word
    }
    const first = word[0]
    const last = word[word.length - 1]
    const temp = first + (word.length - 2).toString() + last
    if (temp.length < word.length) {
        return temp
    }
    return word
}

/*
c4n is h6e
c4n is-h6e
c4n is--h6e
c4n-  -is h6e
 c4n is -h6e
*/
console.log(f('calvin is handsome'))
console.log(f('calvin is-handsome'))
console.log(f('calvin is--handsome'))
console.log(f('calvin-  -is handsome'))
console.log(f(' calvin is -handsome'))