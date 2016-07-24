class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user_follow = {}
        self.timelines = []

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.timelines.append((userId, tweetId))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        followed = self.user_follow.setdefault(userId, set([userId]))
        feeds = []
        for tweet in self.timelines[::-1]:
            if tweet[0] in followed:
                feeds.append(tweet[1])
            if len(feeds) >= 10:
                break
        return feeds

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        followed = self.user_follow.setdefault(followerId, set([followerId]))
        followed.add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        followed = self.user_follow.setdefault(followerId, set([followerId]))
        if followeeId in followed and followerId != followeeId:
            followed.remove(followeeId)

    # Your Twitter object will be instantiated and called as such:
obj = Twitter()
for i in range(100):
    obj.postTweet(1,i)
print(obj.getNewsFeed(1))