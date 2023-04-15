#TC: 
# postTweet, follow, unfollow: O(1)
# getNewsFeed: O(number of followees)

#SC: 
# O(# of users + # of tweets)

class Twitter:

    time = 0

    def __init__(self):
        self.userMap = collections.defaultdict(set)
        self.tweetMap = collections.defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userMap[userId].add(userId)    #follow thyself
        self.tweetMap[userId].append((self.time, tweetId))
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.userMap[userId].add(userId)    #follow thyself
        listOfTweets = []
        for follweeId in self.userMap[userId]:
            for time, tweetId in self.tweetMap[follweeId]:
                if len(listOfTweets)==10:
                    if listOfTweets[0][0]<time: heapq.heappushpop(listOfTweets, (time, tweetId))
                else:
                    heapq.heappush(listOfTweets, (time, tweetId))
        
        ans = []
        while listOfTweets:
            ans.append((heapq.heappop(listOfTweets))[1])
        return ans[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userMap[followerId].add(followerId)
        self.userMap[followeeId].add(followeeId)
        self.userMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userMap[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)