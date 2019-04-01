"""
    1st approach: hashtable + hashset
    - save the users in the hashtable, and save their following users in a hashset
    e.g. connections = {
        'calvin': {'jack', 'jacky', 'bob'},
        'alice': {'peter', 'roy'},
        ....
    }
    - save the tweets with a userId
    e.g. news list = [(userId, tweetId)]
    - every time we get the newsfeed of a user, we iterate backward to look for the tweets which are from his following set

    Time
    - postTweet O(1)
    - getNewsFeed (N)
    - follow average O(1), worst O(n) in a case where all the keys collide
    - follow average O(1), worst O(n) in a case where all the keys collide
    Space   O(M+N) tweets + users conncections
    424 ms, faster than 10.36%
"""


class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.news = []
        self.connections = {}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.news.append((userId, tweetId))
        if userId not in self.connections:
            self.connections[userId] = set([userId])

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        # print(userId)
        # print(self.connections)
        if userId not in self.connections:
            return []
        res = []
        for i in range(len(self.news)-1, -1, -1):
            if self.news[i][0] in self.connections[userId]:
                res.append(self.news[i][1])
                if len(res) == 10:
                    break
        return res

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.connections:
            self.connections[followerId] = set([followerId, followeeId])
        else:
            self.connections[followerId].add(followeeId)

        if followeeId not in self.connections:
            self.connections[followeeId] = set([followeeId])

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId == followeeId:
            return
        if followerId in self.connections:
            if followeeId in self.connections[followerId]:
                self.connections[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
