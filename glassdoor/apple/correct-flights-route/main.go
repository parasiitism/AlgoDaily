package main

import (
	"fmt"
	"strings"
)

/*
	an interesting interview question:
	给一些航线，比如说["SFO-SJC", "SJC-LAX", "LAX-MIA"]，这个例子你就可以从SFO到MIA，但是给的航线的顺序被打乱了，要你输出正确的航线顺序。
	Time		O(n^2)
	Space		O(n)
	18jan2019
*/
func correctFlights(flights []string) []string {
	result := []string{}
	for len(flights) > 0 {
		head := flights[0]
		flights = flights[1:]
		temp := []string{head}
		i := 0
		for i < len(flights) {
			a := strings.Split(temp[len(temp)-1], "-")
			b := strings.Split(flights[i], "-")
			if a[1] == b[0] {
				temp = append(temp, flights[i])
				cop := []string{}
				cop = append(cop, flights[:i]...)
				cop = append(cop, flights[i+1:]...)
				flights = cop
			} else {
				i++
			}
		}
		cop := []string{}
		cop = append(cop, temp...)
		cop = append(cop, result...)
		result = cop
	}
	return result
}

func main() {
	fmt.Println(correctFlights([]string{"SFO-SJC", "SJC-SFO"}))
	fmt.Println(correctFlights([]string{"SFO-SJC", "SJC-LAX", "LAX-MIA"}))
	fmt.Println(correctFlights([]string{"SJC-LAX", "SFO-SJC", "LAX-MIA"}))
	fmt.Println(correctFlights([]string{"A-B", "B-C", "C-D", "D-E", "E-F"}))
	fmt.Println(correctFlights([]string{"D-E", "A-B", "E-F", "B-C", "C-D"}))
}
