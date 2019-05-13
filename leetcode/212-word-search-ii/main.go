package main

/*
	1st approach: naive approach
	- reuse the concept from lc79

	Time	O(k4^N)
	Space	O(4^N)
	640ms beats 23.75%
*/
func findWords(board [][]byte, words []string) []string {
	hashtable := make(map[string]bool)
	for i := 0; i < len(words); i++ {
		word := words[i]
		if exist(board, word) {
			hashtable[word] = true
		}
	}
	result := []string{}
	for k := range hashtable {
		result = append(result, k)
	}
	return result
}

func exist(board [][]byte, word string) bool {
	if len(word) == 0 {
		return false
	}
	// find the "heads" in the matrix
	head := word[0]
	byte_word := []byte(word)
	for row := 0; row < len(board); row++ {
		for col := 0; col < len(board[0]); col++ {
			if board[row][col] == head {
				if dfs(row, col, byte_word, board) {
					return true
				}
			}
		}
	}
	return false
}

func dfs(row int, col int, tail []byte, board [][]byte) bool {
	if row < 0 || row >= len(board) {
		return false
	}
	if col < 0 || col >= len(board[row]) {
		return false
	}
	if board[row][col] != tail[0] {
		return false
	}
	// board[row][col] == tail[0] now
	if len(tail) == 1 {
		return true
	}

	temp := board[row][col]
	board[row][col] = '.'

	t := tail[1:]
	found := dfs(row-1, col, t, board) ||
		dfs(row+1, col, t, board) ||
		dfs(row, col-1, t, board) ||
		dfs(row, col+1, t, board)

	board[row][col] = temp

	return found
}

func main() {

}
