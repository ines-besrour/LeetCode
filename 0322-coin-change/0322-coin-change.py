class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return amount
        dp=[float('inf')]*(amount+1)
        for coin in coins:
            if coin<=amount:
                dp[coin]=1
        for i in range(amount+1):
            for coin in coins:
                if i-coin>0 and dp[i-coin]!=float('inf'):
                    dp[i]=min(dp[i],dp[i-coin]+1)
        return dp[amount] if dp[amount]!=float('inf') else -1
