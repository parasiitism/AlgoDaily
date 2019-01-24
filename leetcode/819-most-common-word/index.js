/*
  takeaway: paragraph.split(/[!?',;. ]/)
  84 ms beats 12.19%
*/

/**
 * @param {string} paragraph
 * @param {string[]} banned
 * @return {string}
 */
var mostCommonWord = function (paragraph, banned) {
  const banned_set = new Set(banned)
  const words = paragraph.split(/[!?',;. ]/) // or paragraph.split(new RegExp("[!?',;. ]", "g"))
  const ht = {}
  for (const word of words) {
    const w = word.toLocaleLowerCase()
    if (banned_set.has(w) || w == "") {
      continue
    }
    if (ht[w] != undefined) {
      ht[w] += 1
    } else {
      ht[w] = 1
    }
  }
  let res_cnt = 0
  let res = ""
  for (const key in ht) {
    if (ht[key] > res_cnt) {
      res_cnt = ht[key]
      res = key
    }
  }
  return res
};

let a = "Bob hit a  ball, the hit BALL flew far after it was hit."
console.log(mostCommonWord(a, ["hit"]))

a = "a, a, a, a, b,b,b,c, c"
console.log(mostCommonWord(a, ["a"]))

a = "Bob!"
console.log(mostCommonWord(a, ["hit"]))