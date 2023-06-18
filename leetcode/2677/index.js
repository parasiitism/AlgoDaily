/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    const chunks = []
    let cur_chunk = []
    for (let i = 0; i < arr.length; i++) {
        if (cur_chunk.length < size) {
            cur_chunk.push(arr[i])
        } else {
            chunks.push(cur_chunk)
            cur_chunk = [arr[i]]
        }
    }
    if (cur_chunk.length > 0) {
        chunks.push(cur_chunk)
    }
    return chunks
};