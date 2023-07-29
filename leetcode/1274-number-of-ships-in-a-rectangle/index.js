/**
 * // This is Sea's API interface.
 * // You should not implement it, or speculate about its implementation
 * function Sea() {
 *     @param {integer[]} topRight
 *     @param {integer[]} bottomLeft
 *     @return {boolean}
 *     this.hasShips = function(topRight, bottomLeft) {
 *         ...
 *     };
 * };
 */


/*
    2nd: DFS + 2-dimension binary search <- iterative
    - divide 1 grid into 4 grids
    - when the left = right and top = bottom, we reach to a point where a ship is
    - see ./idea.png

    Time    O(klogRC)   k = 10 in this problem
    Space   O(klogRC)   the size of queue
    92 ms, faster than 35.90%
*/
var countShips = function(sea, topRight, bottomLeft) {
    const [right, top] = topRight
    const [left, bottom] = bottomLeft
    if (top < bottom || right < left) {
        return 0
    }
    if (!sea.hasShips(topRight, bottomLeft)) {
        return 0
    }
    if (top == bottom && right == left) {
        return 1
    }
    const midX = Math.floor((left + right)/2)
    const midY = Math.floor((top + bottom)/2)
    const bottomLeftCorner = countShips(sea, [midX, midY], bottomLeft)
    const topLeftCorner = countShips(sea, [midX, top], [left, midY+1])
    const topRightCorner = countShips(sea, topRight, [midX+1, midY+1])
    const bottomRightCorner = countShips(sea, [right, midY], [midX+1, bottom])
    return bottomLeftCorner + topLeftCorner + topRightCorner + bottomRightCorner
};