package main

/*
	1st approach: increasing sequence
	- keep track of the last item if the sequence is increasing
	- if the sequence decrease, sum the last-bay to the result and update the bay and last with the current price

	Time    O(n)
	Space   O(1)
	8 ms, faster than 28.13%
*/
func maxProfit(prices []int) int {
	if len(prices) < 2 {
		return 0
	}
	last := prices[0]
	bay := prices[0]
	res := 0
	for i, price := range prices {
		if price >= last {
			last = price
			if i+1 == len(prices) {
				res += last - bay
			}
		} else {
			res += last - bay
			bay = price
			last = price
		}
	}
	return res
}

/*
	2nd approach: increasing sequence
	- optimze the 1st approach
	- actually whenever the current item is larger than the previous item, we can add the diff the result

	Time    O(n)
	Space   O(1)
	4 ms, faster than 100.00%
*/
func maxProfit1(prices []int) int {
	if len(prices) < 2 {
		return 0
	}
	res := 0
	for i := 1; i < len(prices); i++ {
		if prices[i-1] < prices[i] {
			res += prices[i] - prices[i-1]
		}
	}
	return res
}

func main() {

}
