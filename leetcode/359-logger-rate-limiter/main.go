package main

type Logger struct {
	History map[string]int
}

/** Initialize your data structure here. */
func Constructor() Logger {
	return Logger{make(map[string]int)}
}

/*
Returns true if the message should be printed in the given timestamp, otherwise returns false.
If this method returns false, the message will not be printed.
The timestamp is in seconds granularity.
*/
func (this *Logger) ShouldPrintMessage(timestamp int, message string) bool {
	v, x := this.History[message]
	if x {
		if timestamp-v >= 10 {
			this.History[message] = timestamp
			return true
		} else {
			return false
		}
	}
	this.History[message] = timestamp
	return true
}

func main() {

}
