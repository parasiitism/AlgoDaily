package main

import "fmt"

/*
	1st approach got LTE in python
*/

/*
	2nd approach:

	!!! actually i was almost there in 1st approach!!!
	!!! this method is known as topological sorting/ordering !!!

	1. create a list to save to children for each node
	2. for each node, put the children in
			e.g. [4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3]
			children list = [[], [0], [3], [], [3], [2,4,1]]
	3. dfs each node to see if there is a cycle
	4. return true if no cycle

	Time	O(V+E) V: number of vertexes, E: number og edges
	Space	O(V)

	16ms beats 94.81%
*/
func canFinish(numCourses int, prerequisites [][]int) bool {
	// prepare a list to save to children for each node
	graph := [][]int{}
	for i := 0; i < numCourses; i++ {
		graph = append(graph, []int{})
	}
	// iterate though the edges and put them into the corresponding nodes in the graph
	for i := 0; i < len(prerequisites); i++ {
		prereq := prerequisites[i]
		prev := prereq[0]
		cur := prereq[1]
		graph[prev] = append(graph[prev], cur)
	}
	// iterate though the nodes and see if there is a cycle
	seen := make(map[int]int)
	for i := 0; i < len(graph); i++ {
		if dfs(graph, i, seen) == false {
			return false
		}
	}
	return true
}

func dfs(graph [][]int, curIdx int, seen map[int]int) bool {
	if _, x := seen[curIdx]; x {
		if seen[curIdx] == 1 {
			// if seen[curIdx] == 1, it meas this node is being visiting and here is a cycle
			return false
		} else if seen[curIdx] == 2 {
			// if seen[curIdx] == 2, it meas this node has been visited and no cycle is detected
			return true
		}
	}
	// mark the curidx as 'visiting'
	seen[curIdx] = 1
	children := graph[curIdx]
	for i := 0; i < len(children); i++ {
		if dfs(graph, children[i], seen) == false {
			return false
		}
	}
	// mark the curidx as 'visited'
	seen[curIdx] = 2
	return true
}

func main() {
	fmt.Println(canFinish(6, [][]int{
		{4, 3}, {1, 0}, {5, 2}, {5, 4}, {5, 1}, {2, 3},
	}))

	fmt.Println(canFinish(6, [][]int{
		{4, 3}, {1, 0}, {5, 2}, {5, 4}, {5, 1}, {2, 3}, {3, 5},
	}))
}
