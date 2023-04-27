/*
    2nd approach: hashtable
    - move forward the fast pointer until the window contains "satisfies" the target
    - if the window satisfies the target, keep moving the slow pointer to find the minimum window

    e.g. string = azjskfzs, target = az

    first satisfying window
    azjskfzs
    L  R

    move slow(left) pointer to find the minimum
    azjskfzs
     L R

    now the window can not satisfy the target, gonna move the fast(right) poiner next
    azjskfzs
      LR
    
    nice, we see a satisfying window but its length is larger than the intermediate result
    azjskfzs
      L   R
    
    another satisfying window but its length is larger than the intermediate result
    azjskfzs
       L  R
    
    cannot satisfy, move fast pointer next
    azjskfzs
        L R
    
    satisfy now, move the slow pointer next
    azjskfzs
        L  R

    great, this window is satisfying and with shorter length than the intermediate result
    azjskfzs
          LR

    ref:
    - https://www.youtube.com/watch?v=eS6PZLjoaq8

    Time    O(128n) 128 ascii-characters
    Space   O(n)
    328 ms, faster than 5.08%
*/
var minWindow = function(s, t) {
    const ctr_t = count_alphabet(t)
    const ctr_s = Array(128).fill(0)
    let j = 0
    let res_length = 2**32
    let res = ''
    for (let i = 0 ; i < s.length; i++) {
        const right = s[i]
        ctr_s[right.charCodeAt()] += 1
        while (s_contains_t(ctr_s, ctr_t)) {
            const left = s[j]
            ctr_s[left.charCodeAt()] -= 1
            if (i - j + 1 < res_length) {
                res = s.slice(j, i+1)
                res_length = i - j + 1
            }
            j += 1
        }
    }
    return res
};

const count_alphabet = T => {
    const ctr = Array(128).fill(0)
    for (let c of T) {
        ctr[c.charCodeAt()] += 1
    }
    return ctr
}

const s_contains_t = (A, B) => {
    for (let i = 0 ; i < 128; i++) {
        if (A[i] < B[i]) {
            return false
        }
    }
    return true
}

/*
    same as 1st but use indices to compare
*/
var minWindow = function(s, t) {
    const targetHt = {}
    for (let c of t) {
        if (c in targetHt === false) {
            targetHt[c] = 0
        }
        targetHt[c] += 1
    }
    const curHt = {}
    
    let j = 0
    
    let _j = 0
    let _i = s.length + 1
    
    for (let i = 0; i < s.length; i++) {
        const c = s[i]
        
        if (c in curHt === false) {
            curHt[c] = 0
        }
        curHt[c] += 1
        
        while (curContainTarget(curHt, targetHt)) {
            
            if (i - j + 1 < _i - _j + 1) {
                _i = i
                _j = j
            }
            
            const left = s[j]
            j += 1
            curHt[left] -= 1
        }
    }
    if (_i == s.length + 1) {
        return ''
    }
    return s.slice(_j, _i + 1)
};

const curContainTarget = (curHt, targetHt) => {
    for (let key in targetHt) {
        if (key in curHt === false) {
            return false
        }
        if (curHt[key] < targetHt[key]) {
            return false
        }
    }
    return true
}