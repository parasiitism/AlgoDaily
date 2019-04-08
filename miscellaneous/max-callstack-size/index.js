function calMaxCallStack() {
	try {
		return calMaxCallStack() + 1
	} catch (error) {
		return 1
	}
}

// node: 13926
console.log(calMaxCallStack())