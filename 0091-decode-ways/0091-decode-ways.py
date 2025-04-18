class Solution:
    def numDecodings(self, s: str) -> int:
        memo={len(s):1}
        def helper(i):
            if i in memo:
                return memo[i]
            if s[i]=='0':
                return 0
            res=helper(i+1)
            if i+2<=len(s) and int(s[i:i+2])<27:
                res+=helper(i+2)
            memo[i]=res
            return memo[i]
        return helper(0)
        

