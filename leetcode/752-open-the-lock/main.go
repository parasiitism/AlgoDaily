package main

import (
	"fmt"
	"math"
)

type Queue struct {
	Node  string
	Depth int
}

func openLock(deadends []string, target string) int {

	if len(target) == 0 {
		return -1
	}

	deadends_hash := make(map[string]bool)
	for i := 0; i < len(deadends); i++ {
		deadends_hash[deadends[i]] = true
	}

	visited := make(map[string]bool)

	minSteps := math.MaxInt32

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
		if node == target && steps < minSteps {
			minSteps = steps
		} else {
			// for every digit
			for i := 0; i < len(node); i++ {
				digit := node[i]
				// -1
				var dec string
				if digit == '0' {
					dec = "9"
				} else {
					dec = string(digit - 1)
				}
				queue = append(queue, Queue{node[:i] + dec + node[i+1:], steps + 1})
				// +1
				var inc string
				if digit == '9' {
					inc = "0"
				} else {
					inc = string(digit + 1)
				}
				queue = append(queue, Queue{node[:i] + inc + node[i+1:], steps + 1})
			}
		}
	}
	if minSteps == math.MaxInt32 {
		return -1
	}
	return minSteps
}

func main() {
	// a := '0'
	// fmt.Println(string(a - 1))
	a := []string{"0201", "0101", "0102", "1212", "2002"}
	b := "0202"
	fmt.Println(openLock(a, b))
}
