class Solution:
    def numSquares(self, n: int) -> int:
        dp=[float('inf')]*(n+1)
        perfect=set()
        for i in range(1,n+1):
            if sqrt(i).is_integer():
                dp[i]=1
                perfect.add(i)
        for i in range(n+1):
            for p in perfect:
                if i-p>0 and dp[i-p]!=float('inf'):
                    dp[i]=min(dp[i-p]+1,dp[i])
        return dp[n]

             
            