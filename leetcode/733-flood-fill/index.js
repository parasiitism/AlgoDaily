
/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
var floodFill = function(image, sr, sc, color) {
    const R = image.length
    const C = image[0].length
    const orig = image[sr][sc]
    if (orig == color) {
        return image
    }
    const q = [[sr, sc]]
    while (q.length > 0) {
        const [i, j] = q.shift()
        
        if (i < 0 || i > R-1 || j < 0 || j > C-1) {
            continue
        }
        if (image[i][j] !== orig) {
            continue
        }
        image[i][j] = color
        q.push([i-1,j])
        q.push([i+1,j])
        q.push([i,j-1])
        q.push([i,j+1])
    }
    return image
};