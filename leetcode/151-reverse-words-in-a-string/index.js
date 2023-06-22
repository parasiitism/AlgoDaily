var reverseWords = function(s) {
    const S = s.trim()
    const words = S.split(" ").filter(x => x.length > 0)
    words.reverse()
    return words.join(" ")
};