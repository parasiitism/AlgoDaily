package main

import "fmt"

/*
	1st approach: topological ordering in bfs using queue
	1. construct the edges
	2. topo sort

	Time    O(V+E)
	Space   O(V)
	0 ms, faster than 100.00%
*/
func alienOrder(words []string) string {
	edges := [][]string{}
	nodeSet := make(map[string]bool)
	// put the characters in order into the edges
	for i := 0; i < len(words); i++ {
		word := words[i]
		edgeFormed := false
		for j := 0; j < len(word); j++ {
			nodeSet[string(word[j])] = true
			if !edgeFormed && i > 0 && j < len(words[i-1]) && words[i-1][j] != words[i][j] {
				// construct graph, [to, from]
				prev := string(words[i-1][j])
				cur := string(words[i][j])
				edges = append(edges, []string{prev, cur})
				edgeFormed = true
			}
		}
	}
	// set to list
	nodes := []string{}
	for key := range nodeSet {
		nodes = append(nodes, key)
	}
	// topsort
	arr := topoBFS(edges, nodes)
	result := ""
	for _, s := range arr {
		result += s
	}
	return result
}

func topoBFS(prerequisites [][]string, nodes []string) []string {
	// indegrees
	indegrees := make(map[string]int)
	for _, node := range nodes {
		indegrees[node] = 0
	}
	// connections
	connections := make(map[string][]string)
	for _, pre := range prerequisites {
		src := pre[0]
		dest := pre[1]
		if _, x := connections[src]; !x {
			connections[src] = []string{dest}
		} else {
			connections[src] = append(connections[src], dest)
		}
		//add indegree for each node
		indegrees[dest]++
	}
	// get the nodes with 0 indegree
	queue := []string{}
	for key := range indegrees {
		if indegrees[key] == 0 {
			queue = append(queue, key)
		}
	}
	// dequeue node from the queue and put it into the result
	res := []string{}
	for len(queue) > 0 {
		dq := queue[0]
		queue = queue[1:]
		res = append(res, dq)
		if _, x := connections[dq]; x {
			children := connections[dq]
			for _, child := range children {
				indegrees[child]--
				if indegrees[child] == 0 {
					queue = append(queue, child)
				}
			}
		}
	}
	// return [] if there is a cycle
	for key := range indegrees {
		if indegrees[key] > 0 {
			return []string{}
		}
	}
	return res
}

/*
	2nd approach: topological ordering in dfs using recursion and stack
	1. construct the edges
	2. topo sort

	Time    O(V+E)
	Space   O(V)
	0 ms, faster than 100.00%
*/
func alienOrder1(words []string) string {
	edges := [][]string{}
	nodeSet := make(map[string]bool)
	// put the characters in order into the edges
	for i := 0; i < len(words); i++ {
		word := words[i]
		edgeFormed := false
		for j := 0; j < len(word); j++ {
			nodeSet[string(word[j])] = true
			if !edgeFormed && i > 0 && j < len(words[i-1]) && words[i-1][j] != words[i][j] {
				// construct graph, [to, from]
				prev := string(words[i-1][j])
				cur := string(words[i][j])
				edges = append(edges, []string{prev, cur})
				edgeFormed = true
			}
		}
	}
	// set to list
	nodes := []string{}
	for key := range nodeSet {
		nodes = append(nodes, key)
	}
	// topsort
	arr := topoDFS(edges, nodes)
	result := ""
	for _, s := range arr {
		result += s
	}
	return result
}

func topoDFS(prerequisites [][]string, nodes []string) []string {
	// connections
	connections := make(map[string][]string)
	for _, pre := range prerequisites {
		src := pre[0]
		dest := pre[1]
		if _, x := connections[src]; !x {
			connections[src] = []string{dest}
		} else {
			connections[src] = append(connections[src], dest)
		}
	}
	seen := make(map[string]int)
	stack := []string{}
	// the inner function of dfs
	var exploreVertex func(curKey string) bool
	exploreVertex = func(curKey string) bool {
		seen[curKey] = 1
		children := connections[curKey]
		for i := 0; i < len(children); i++ {
			child := children[i]
			if v, x := seen[child]; x {
				if v == 1 {
					// if seen[curIdx] == 1, it meas this node is being visiting and here is a cycle
					return false
				} else if v == 2 {
					// if seen[curIdx] == 2, it meas this node has been visited and no cycle is detected
					continue
				}
			}
			if exploreVertex(child) == false {
				return false
			}
		}
		// mark the curidx as 'visited'
		seen[curKey] = 2
		stack = append(stack, curKey)
		return true
	}
	// start to iterate the nodes
	for i := 0; i < len(nodes); i++ {
		node := nodes[i]
		if v, x := seen[node]; x {
			if v == 1 {
				return []string{}
			} else if v == 2 {
				continue
			}
		}
		if exploreVertex(node) == false {
			return []string{}
		}
	}
	res := []string{}
	for i := len(stack) - 1; i >= 0; i-- {
		res = append(res, stack[i])
	}
	return res
}

func main() {
	a := []string{
		"wrt",
		"wrf",
		"er",
		"ett",
		"rftt",
	}
	fmt.Println(alienOrder1(a))

	a = []string{
		"z",
		"x",
	}
	fmt.Println(alienOrder1(a))

	a = []string{
		"z",
		"x",
		"z",
	}
	fmt.Println(alienOrder1(a))

	a = []string{
		"z",
		"z",
	}
	fmt.Println(alienOrder1(a))

	a = []string{
		"za",
		"zb",
		"ca",
		"cb",
	}
	fmt.Println(alienOrder1(a))
}
