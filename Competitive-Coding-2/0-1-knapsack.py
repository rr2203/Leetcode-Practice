#TC: O(n*capactiy)
#SC: O(n*capactiy)
weights=[60,7,8,5,50,10]
values=[600,500,400,200,300,20]
capacity=60
def knapSack(self,capacity, weights, values, n):
        dp=[[0]*(capacity+1) for _ in range(n+1)]
    
        for i in range(n-1,-1,-1):
            for j in range(1,capacity+1):
                dp[i][j]=dp[i+1][j]
                if j-weights[i] >=0:
                    dp[i][j]=max(dp[i][j], values[i]+dp[i+1][j-weights[i]])
                    
        return dp[0][capacity]