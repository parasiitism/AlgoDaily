"""
    hashtable

    Time of upload      O(1)
    Time of longest     O(N) worst
    Space               O(N)
    1184 ms, faster than 50.00%
"""


class LUPrefix:

    def __init__(self, n: int):
        self.n = n
        self.videos = n * [False]
        self.cached_length = 0

    def upload(self, video: int) -> None:
        self.videos[video-1] = True

    def longest(self) -> int:
        n = self.n
        s = self.cached_length
        e = n
        for i in range(s, self.n):
            if self.videos[i] == False:
                e = i
                break
        self.cached_length = e
        return e


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
