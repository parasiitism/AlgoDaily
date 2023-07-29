/*
    lets say u r give a string and a character, find the shortest index distance from every character to the target character

    e.g.
    s = 'bloomberg', target = 'b'

    result = [0, 1, 2, 2, 1, 0, 1, 2, 3]

    Explanation:
    
    b l o o m b e r g
    0 1 2 2 1 0 1 2 3
      < < > >   < < <

    Assume the input only allows lowercase letters
*/

/*
    Approach

        b l o o m b e r g
    ->  0 1 2 3 4 0 1 2 3
    <-  0 4 3 2 1 0 * * *
        -----------------
        0 1 2 2 1 0 1 2 3 <- result
*/
const shortestDistances = (s, target) => {
    const n = s.length
    let left_target_idx = null
    const distances = Array(n).fill(2**32)
    for (let i = 0; i < n; i++) {
        if (s[i] == target) {
            left_target_idx = i
        }
        if (left_target_idx != null) {
            distances[i] = i - left_target_idx
        }
    }

    let right_target_idx = null
    for (let i = n-1; i >= 0; i--) {
        if (s[i] == target) {
            right_target_idx = i
        }
        if (right_target_idx != null) {
            distances[i] = Math.min(distances[i], right_target_idx - i)
        }
    }

    return distances
}

let a, b

a = 'bloomberg'
b = 'b'
console.log(shortestDistances(a, b))

a = 'bloomberg'
b = 'z'
console.log(shortestDistances(a, b))