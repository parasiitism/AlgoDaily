"""
    1st: hashing
"""


class Codec:

    def __init__(self):
        self.arr = []

    def _numToBase62(self, num):
        base62 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        hashval = ""
        while True:
            hashval = base62[num % 62] + hashval
            num /= 62
            if num == 0:
                break
        return hashval

    def _base62ToNum(self, s):
        base62 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        num = 0
        for ss in s:
            num = num*62 + base62.index(ss)
        return num

    def encode(self, longUrl):
        self.arr.append(longUrl)
        hashval = self._numToBase62(len(self.arr)-1)
        return "http://tinyurl.com/"+hashval

    def decode(self, shortUrl):
        shatters = shortUrl.split("/")
        return self.arr[self._base62ToNum(shatters[-1])]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
