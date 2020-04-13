# coding: utf-8
# letcode 355
from typing import List

class ID:
    index = 0

class Tweet:
    def __init__(self, tweetId):
        ID.index += 1
        self.tweetId = tweetId
        self.time = ID.index


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.userTweets = {}
        self.userFollows = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        tweet = Tweet(tweetId)
        if userId not in self.userTweets:
            self.userTweets[userId] = []
        if tweetId not in self.userTweets[userId]:
            self.userTweets[userId].append(tweet)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        tweets = []
        if userId in self.userTweets:
            selfTweets = self.userTweets[userId]
            for tweet in selfTweets:
                tweets.append(tweet)

        if userId in self.userFollows:
            followeeIds = self.userFollows[userId]
            for followeeId in followeeIds:
                if followeeId in self.userTweets:
                    for tweet in self.userTweets[followeeId]:
                        tweets.append(tweet)
        # 排序
        tweets.sort(key=lambda tweet: tweet.time, reverse=True)

        latest = []
        for t in tweets[0: 10]:
            latest.append(t.tweetId)
        return latest

        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            if followerId not in self.userFollows:
                self.userFollows[followerId] = []
            if followeeId not in self.userFollows[followerId]:
                self.userFollows[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            if followerId in self.userFollows:
                followeeIds = self.userFollows[followerId]
                if followeeIds:
                    if followeeId in followeeIds:
                        for v in followeeIds:
                            if v == followeeId:
                                followeeIds.remove(v)
                                break

        


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1,1)
param_2 = obj.getNewsFeed(1)
obj.follow(1, 2)
obj.unfollow(1,2)