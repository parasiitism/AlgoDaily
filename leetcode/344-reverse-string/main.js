/*
  the purpose of the question is to use 2 pointers, so i am just gonna implement it with 2 pointers
  208ms beats 2.54% 
*/
var reverseString = function (s) {
  var i = 0
  var j = s.length - 1
  while (i < j) {
    const temp = s[i]
    s[i] = s[j]
    s[j] = temp
    i++
    j--
  }
};

var a = ["h", "e", "l", "l", "o"]
reverseString(a)
console.log(a)