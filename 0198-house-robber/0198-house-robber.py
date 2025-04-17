class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        dp=[0]*len(nums)
        dp[0],dp[1],dp[2]=nums[0],nums[1],max(nums[2]+nums[0],nums[1])
        for i in range(3,len(nums)):
            dp[i]=max(dp[i-2]+nums[i],nums[i]+dp[i-3])
        return max(dp[-1],dp[-2])
