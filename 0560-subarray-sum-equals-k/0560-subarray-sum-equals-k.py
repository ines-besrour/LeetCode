class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref,res=0,0
        countPrefSum={0:1}
        for i in range(len(nums)):
            pref+=nums[i]
            if pref-k in countPrefSum:
                res+=countPrefSum[pref-k]
            if pref not in countPrefSum:
                countPrefSum[pref]=1
            else:
                countPrefSum[pref]+=1
        return res
