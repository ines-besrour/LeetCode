class Solution:
    def rob(self, nums: List[int]) -> int:
        length=len(nums)
        if length<=1:
            return sum(nums)
        dp=[0]*length
        dp[0],dp[1]=nums[0],nums[1]
        for i in range(2,length):
            if i==2:
                dp[i]=nums[i]+dp[i-2]
            else:
                dp[i]=nums[i]+max(dp[i-2],dp[i-3])
        return max(dp[-1],dp[-2])

