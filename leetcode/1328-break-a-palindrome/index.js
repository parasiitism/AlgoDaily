/*
    1st: string
    - the basic idea is to find make the first character after 'a' to an 'a'
    - but there are some corner cases where if we change an char, the string will still be a palindrome, so we should change the final char to 'b'
    e.g.
    - aaaaaa -> aaaaab
    - aabaa -> aabab
    - aacaa -> aacab

    Time    O(N)
    Space   O(N)
    16 ms, faster than 74.73%
*/
var breakPalindrome = function(palindrome) {
    const n = palindrome.length;
    if (n <= 1) {
      return ""
    }
    for (let i = 0; i < Math.floor(n/2); i++) {
      const c = palindrome[i]
      if (c != "a") {
        return palindrome.slice(0, i) + "a" + palindrome.slice(i+1)
      }
    }
    return palindrome.slice(0, n-1) + 'b'
  };