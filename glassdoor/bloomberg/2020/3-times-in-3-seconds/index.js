/*
    https://leetcode.com/discuss/interview-question/522824/Bloomberg-or-Phone-or-New-Grad-SWE-(London)-next-round

    Write a function which returns True if called more than 3 times in 3 seconds

    Time    O(N)
    Space   O(K)
*/
function atLeast3Times() {
    let timestamps = [];
  
    return function() {
        const now = Date.now();
        timestamps = timestamps.filter((timestamp) => now - timestamp <= 3000);
        timestamps.push(now);
        return timestamps.length > 3;
    };
  }
  
// e.g:
let check = atLeast3Times();

console.log(check()); // false
console.log(check()); // false
console.log(check()); // false
console.log(check()); // true (3-second window exceeded)
console.log(check()); // true (still within the 3-second window)

console.log("--- make it generic ---")

function atLeast3Times2(fn, interval=3000, limit=3) {
    let timestamps = [];
  
    return function(...args) {
        const now = Date.now();
        fn(...args)
        timestamps = timestamps.filter((timestamp) => now - timestamp <= interval);
        timestamps.push(now);
        return timestamps.length > limit;
    };
  }
  
// e.g:
check = atLeast3Times2(()=> console.log('hi'), 3000, 3);

console.log(check()); // false
console.log(check()); // false
console.log(check()); // false
console.log(check()); // true (3-second window exceeded)
console.log(check()); // true (still within the 3-second window)