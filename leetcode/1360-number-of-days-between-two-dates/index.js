/**
 * @param {string} date1
 * @param {string} date2
 * @return {number}
 */
/*
    1st: use built-in method

    Time    O(N)
    Space   O(1)
    52 ms, faster than 75.68%
*/
var daysBetweenDates = function(date1, date2) {
	const a = new Date(date1).getTime(),
		b = new Date(date2).getTime();
	return Math.round(Math.abs(a - b) / (1000 * 60 * 60 * 24));
};
