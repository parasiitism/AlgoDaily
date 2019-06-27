function balenceParentheses(s) {
  let res = 0
  const stack = []
  for (let i = 0; i < s.length; i++) {
    const c = s[i]
    if (c == "(") {
      stack.push(c)
    } else if (c == ")") {
      if (stack.length == 0) {
        res++
      } else {
        stack.pop()
      }
    }
  }
  return res + stack.length
}

console.log(balenceParentheses(""))
console.log(balenceParentheses("()"))
console.log(balenceParentheses(")(("))
console.log(balenceParentheses("()((())"))
console.log(balenceParentheses("()))(("))
console.log(balenceParentheses("()())()"))