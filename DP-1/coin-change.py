#TC: O(n*target)
#SC: O(n*target)
class Solution:
    def coinChange(self, coins: List[int], target: int) -> int:
        n = len(coins)
        dp = [[target+1]*(target+1) for _ in range(n+1)]

        for i in range(n,-1,-1):
            for cur_target in range(0,target+1):
                if cur_target==0:
                    dp[i][cur_target]=0
                elif i!=n: 
                    dp[i][cur_target] = dp[i+1][cur_target]
                    if cur_target-coins[i]>=0:
                        dp[i][cur_target] = min(dp[i][cur_target],1+dp[i][cur_target-coins[i]])

        return dp[0][target] if dp[0][target]!=target+1 else -1