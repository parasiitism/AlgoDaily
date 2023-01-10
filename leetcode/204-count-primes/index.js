/*
    hashtable

    ref:
    - https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    Time    O(N log (log N)) <- according to the article
    Space   O(N)
    136 ms, faster than 81.25%
*/
var countPrimes = function(n) {
    const arePrimes = Array(n).fill(true)
    arePrimes[0] = false
    arePrimes[1] = false
    for (let i = 2; i*i <= n; i++) {
        if (arePrimes[i] === false) {
            continue
        }
        for (let j = i; i*j <= n; j++) {
            arePrimes[i*j] = false
        }
    }
    const primes = []
    for (let i = 0; i < arePrimes.length; i++) {
        if (arePrimes[i] === true) {
            primes.push(i)
        }
    }
    return primes.length
};