package main

/*
   1st approach: iterative dfs

   Time    O(n)
	 Space   O(n)
	 4 ms, faster than 100.00%
*/
func canVisitAllRooms(rooms [][]int) bool {
	if len(rooms) == 0 {
		return false
	}
	ht := make(map[int]bool)
	ht[0] = true
	stack := []int{}
	for _, key := range rooms[0] {
		stack = append(stack, key)
	}
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if _, x := ht[pop]; x {
			continue
		}
		ht[pop] = true
		for _, key := range rooms[pop] {
			stack = append(stack, key)
		}
	}

	for i := 0; i < len(rooms); i++ {
		if _, x := ht[i]; !x {
			return false
		}
	}
	return true
}

func main() {

}
