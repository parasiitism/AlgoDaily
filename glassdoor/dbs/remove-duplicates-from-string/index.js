/*
  questions:
  - input only has lowercase letter? yes
  - so i need to put them in order? yes, in the original string order
*/

function dedup(s) {
  // 26*[0]
  const seen = []
  for (let i = 0; i < 26; i++) {
    seen.push(false)
  }
  // loop over the characters
  for (let i = 0; i < s.length; i++) {
    const c = s[i]
    const key = c.charCodeAt(0) - 97
    seen[key] = true
  }
  // loop again to construct result
  let res = ""
  for (let i = 0; i < s.length; i++) {
    const c = s[i]
    const key = c.charCodeAt(0) - 97
    if (seen[key] == true) {
      res += c
      seen[key] = false
    }
  }
  return res
}

console.log(dedup("geeksforgeeks"))
console.log(dedup("characters"))