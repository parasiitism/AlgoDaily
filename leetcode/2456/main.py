"""
    hashtable + sort

    Time    O(C+VlogV)
    Space   O(2C)
    4387 ms, faster than 16.67%
"""


class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        n = len(creators)
        creators_views = Counter()
        creators_videos = defaultdict(list)
        for i in range(n):
            c = creators[i]
            vid = ids[i]
            v = views[i]
            creators_views[c] += v
            creators_videos[c].append((vid, v))
        highest = 0
        most_popular = []
        for c in creators_views:
            v = creators_views[c]
            if v > highest:
                highest = v
                most_popular = [c]
            elif v == highest:
                most_popular.append(c)
        res = []
        for c in most_popular:
            vids = creators_videos[c]
            vids.sort(key=lambda x: (-x[1], x[0]))
            res.append([c, vids[0][0]])
        return res
