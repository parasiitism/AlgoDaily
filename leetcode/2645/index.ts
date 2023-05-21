/*
    greedy
    - a:
        - skip bc if exist
        - skip b, add c 
        - add b, skip c
        - add ab
    - b: add a at the front
        - skip c if exist
        - add c
    - c: add ab at the front

    Time    O(N)
    Space   O(1)
*/
function addMinimum(word: string): number {
    const n = word.length
    let i = 0
    let to_add = 0
    while (i < n) {
        const c = word[i]
        if (c === 'a') {
            if (i+2 < n && word[i+1] == 'b' && word[i+2] == 'c') {
                i += 2
            } else if (i+1 < n && word[i+1] == 'b') {
                to_add += 1
                i += 1
            } else if (i+1 < n && word[i+1] == 'c') {
                to_add += 1
                i += 1
            } else {
                to_add += 2
            }
        } else if (c === 'b') {
            to_add += 1
            if (i+1 < n && word[i+1] == 'c') {
                i += 1
            } else {
                to_add += 1
            }
        } else {
            to_add += 2
        }
        i += 1
    }
    return to_add
};