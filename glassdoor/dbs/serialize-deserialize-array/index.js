/*
  https://www.geeksforgeeks.org/serialize-deserialize-array-string/
*/

// [abc, de] => 3abc2de
function serialize(arr) {
  let temp = ""
  for (let i = 0; i < arr.length; i++) {
    let s = arr[i]
    let l = arr[i].length
    temp += l.toString() + s
  }
  return temp
}

// 3abc2de => [abc, de]
function deserialize(s) {
  const res = []
  let i = 0
  while (i < s.length) {
    const cnt = parseInt(s[i])
    let temp = s.slice(i + 1, i + 1 + cnt) // similar to s[a:b]
    res.push(temp)
    i = i + 1 + cnt
  }
  return res
}

let s = serialize(["abc", "ab", "1"])
console.log(s)
let d = deserialize(s)
console.log(d)

s = serialize(["geeks", "are", "awesome"])
console.log(s)
d = deserialize(s)
console.log(d)

s = serialize(["hello", "guys", "whats", "up!!!"])
console.log(s)
d = deserialize(s)
console.log(d)

s = serialize([])
console.log(s)
d = deserialize(s)
console.log(d)

s = serialize([""])
console.log(s)
d = deserialize(s)
console.log(d)