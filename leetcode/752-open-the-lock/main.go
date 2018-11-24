package main

import (
	"fmt"
	"strconv"
)

type Queue struct {
	Node  string
	Depth int
}

func openLock(deadends []string, target string) int {
	if len(target) == 0 {
		return -1
	}
	// search optimization
	deadends_hash := make(map[string]bool)
	for i := 0; i < len(deadends); i++ {
		deadends_hash[deadends[i]] = true
	}
	// for visited paths
	visited := make(map[string]bool)
	// iterate the mutations
	var queue []Queue
	queue = append(queue, Queue{"0000", 0})
	for len(queue) > 0 {
		head := queue[0]
		queue = queue[1:]
		node := head.Node
		steps := head.Depth
		if _, existed := visited[node]; existed {
			continue
		}
		visited[node] = true
		if _, existed := deadends_hash[node]; existed {
			continue
		}
		if node == target {
			return steps
		} else {
			// for every digit
			for i := 0; i < len(node); i++ {
				digit := int(node[i] - '0')
				// -1
				dec := strconv.Itoa((digit + 9) % 10)
				queue = append(queue, Queue{node[:i] + dec + node[i+1:], steps + 1})
				// +1
				inc := strconv.Itoa((digit + 1) % 10)
				queue = append(queue, Queue{node[:i] + inc + node[i+1:], steps + 1})
			}
		}
	}
	return -1
}

func main() {
	a := []string{"0201", "0101", "0102", "1212", "2002"}
	b := "0202"
	fmt.Println(openLock(a, b))
}
