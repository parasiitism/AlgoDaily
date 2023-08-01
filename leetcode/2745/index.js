/*
    Math
    - there are x of AA, y of BB, z of AB

    - for AB
        - on its left we can only have BB - e.g. BB + AB
        - on its right we can only have AA - e.b. AB + AA
    It means that we now simplified the problem to: Find the longest AABB....AABB or BBAA....BBAA, and the append AB...AB

*/
var longestString = function(x, y, z) {
    const couple = Math.min(x, y)
    if (x === y) {
        return (couple*2 + z) * 2
    }
    return (couple*2 + 1 + z) * 2
};