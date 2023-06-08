# TC: O(n) | SC: O(n)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for i in range(n-1):
            if ratings[i+1] > ratings[i] and candies[i+1] <= candies[i]:
                candies[i+1] = candies[i] + 1
        for i in range(n-1, 0, -1):
            if ratings[i-1] > ratings[i] and candies[i-1] <= candies[i]:
                candies[i-1] = candies[i] + 1

        return sum(candies)