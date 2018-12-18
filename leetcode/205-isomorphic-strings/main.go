package main

import (
	"fmt"
	"strconv"
)

// naive solution
// 1 map for order plus 1 arry for occurrence for each string
// beats 1.00%
func isIsomorphic(s string, t string) bool {
	hash1 := make(map[string]int)
	hash1map := []string{}
	hash2 := make(map[string]int)
	hash2map := []string{}

	for i := 0; i < len(s); i++ {
		cur := string(s[i])
		v, ex := hash1[cur]
		if ex {
			hash1map[v] += "," + strconv.Itoa(i)
		} else {
			hash1map = append(hash1map, strconv.Itoa(i))
			hash1[cur] = len(hash1map) - 1
		}
	}

	for i := 0; i < len(t); i++ {
		cur := string(t[i])
		v, ex := hash2[cur]
		if ex {
			hash2map[v] += "," + strconv.Itoa(i)
		} else {
			hash2map = append(hash2map, strconv.Itoa(i))
			hash2[cur] = len(hash2map) - 1
		}
	}
	if len(hash1) != len(hash2) || len(hash1map) != len(hash2map) {
		return false
	}
	for i := 0; i < len(hash1map); i++ {
		if hash1map[i] != hash2map[i] {
			return false
		}
	}
	return true
}

// optimal
// just save the last occurrent idx of each charactor
// beats 5.88%
// I dont know why it gets so slow. Actually, it is very similar to the 'common' solution which beats 50%
func isIsomorphic1(s string, t string) bool {
	hashS, hashT := make(map[byte]int), make(map[byte]int)
	for i := 0; i < len(s); i++ {
		curS, curT := s[i], t[i]
		_, exS := hashS[curS]
		_, exT := hashT[curT]
		if !exS && !exT { // both not exist
			hashS[curS] = i
			hashT[curT] = i
		} else if exS && exT { // both find the last idx of corresponding cur in corresponding hashtable
			if hashS[curS] != hashT[curT] {
				return false // the last indexes are not the sames
			}
			hashS[curS] = i
			hashT[curT] = i
		} else {
			return false // one exists but it counterpart doesnt
		}
	}
	return true
}

func main() {
	// m := make(map[string]string)
	// m["c"] = "cc"
	// m["b"] = "bb"
	// m["a"] = "bb"
	// m["c"] += "d"
	// fmt.Println(m)
	// fmt.Println(reflect.ValueOf(m).MapKeys())
	// fmt.Println(m["a"] == m["c"])
	fmt.Println(isIsomorphic1("paper", "title"))
}
