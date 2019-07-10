/*
I was asked in an interview about this
Find the max number of words in sentences
e.g.
"We test coders. Give us a try? hey" return 4 becos length of [Give, us, a, try] is 4
e.g.2
"Forget  CVs..Save time . x x" return 2 becos length of [x, x] is 2
*/

function yo(S) {
  let res = 0;
  let b = S.split(new RegExp('[.?!]', 'g'))
  for (let i = 0; i < b.length; i++) {
    console.log(b)
    // const c = b[i].trim().split(/\s+/g)
    const c = b[i].trim().split(' ')
    console.log(c)
    if (c.length > res) {
      res = c.length
    }
  }
  console.log(res)
  return res
}

yo('We test coders. Give us a try? hey')
yo('Forget  CVs..Save time . x x')

// var separators = [' ', '\\\+', '-', '\\\(', '\\\)', '\\*', '/', ':', '\\\?'];
// console.log(separators.join('|'));
// var tokens = x.split(new RegExp(separators.join('|'), 'g'));
// console.log(tokens);