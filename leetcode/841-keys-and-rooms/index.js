/**
 * @param {number[][]} rooms
 * @return {boolean}
 */
var canVisitAllRooms = function(rooms) {
    const q = [0]
    const visited = new Set()
    while (q.length > 0) {
        const node = q.shift()
        if (visited.has(node)) {
            continue
        }
        visited.add(node)
        for (let nb of rooms[node]) {
            q.push(nb)
        }
    }
    return visited.size === rooms.length
};