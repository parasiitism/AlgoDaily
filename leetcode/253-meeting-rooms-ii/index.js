/*
    1st approach
    - sort the array
    - create an array to store the end time of the latest meeting in every room
    - each interval, compare the last meeting(since sorted) amongst the meeting in the meeting rooms
    - if there is no collision, put the meeting in that room, else create a new meeting room for the interval

    Time		O(NlogN)    sort
    Space 	    O(N)	    result array
    104 ms, faster than 35.74%
*/
var minMeetingRooms = function(intervals) {
    const ends = []
    intervals.sort((a, b) => {
        if (a[0] == b[0]) { return a[1] - b[1] }
        return a[0] - b[0]
    })
    for (let [s, e] of intervals) {
        if (ends.length == 0) {
            ends.push(e)
        } else {
            let earliest = ends[0]
            let earliest_idx = 0
            for (let i = 1; i < ends.length; i++) {
                if (ends[i] < earliest) {
                    earliest = ends[i]
                    earliest_idx = i
                }
            }
            if (earliest <= s) {
                ends[earliest_idx] = e
            } else {
                ends.push(e)
            }
        }
    }
    return ends.length
};
