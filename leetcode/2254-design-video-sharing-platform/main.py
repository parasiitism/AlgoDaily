from heapq import *
from collections import *

"""
    hashtable, minheap

    Time of upload()            O(logN)
    Time of upload()            O(logN)
    Time of other functions     O(1)
    936 ms, faster than 20.83%
"""


class VideoSharingPlatform:

    def __init__(self):
        self.next_v_id = 0
        self.dump_ids = []
        self.key2video = defaultdict(Video)

    def upload(self, video: str) -> int:
        v_id = None
        if len(self.dump_ids) > 0:
            v_id = heappop(self.dump_ids)
        else:
            v_id = self.next_v_id
            self.next_v_id += 1
        self.key2video[v_id] = Video(video)
        return v_id

    def remove(self, videoId: int) -> None:
        if videoId not in self.key2video:
            return
        heappush(self.dump_ids, videoId)
        del self.key2video[videoId]

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId not in self.key2video:
            return '-1'
        obj = self.key2video[videoId]
        video = obj.content
        if startMinute >= len(video):
            return '-1'
        self.key2video[videoId].views += 1
        return video[startMinute: min(endMinute, len(video) - 1) + 1]

    def like(self, videoId: int) -> None:
        if videoId not in self.key2video:
            return
        self.key2video[videoId].like += 1

    def dislike(self, videoId: int) -> None:
        if videoId not in self.key2video:
            return
        self.key2video[videoId].dislike += 1

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if videoId not in self.key2video:
            return [-1]
        a = self.key2video[videoId].like
        b = self.key2video[videoId].dislike
        return [a, b]

    def getViews(self, videoId: int) -> int:
        if videoId not in self.key2video:
            return -1
        return self.key2video[videoId].views


class Video:
    def __init__(self, video):
        self.content = video
        self.views = 0
        self.like = 0
        self.dislike = 0

# Your VideoSharingPlatform object will be instantiated and called as such:
# obj = VideoSharingPlatform()
# param_1 = obj.upload(video)
# obj.remove(videoId)
# param_3 = obj.watch(videoId,startMinute,endMinute)
# obj.like(videoId)
# obj.dislike(videoId)
# param_6 = obj.getLikesAndDislikes(videoId)
# param_7 = obj.getViews(videoId)
