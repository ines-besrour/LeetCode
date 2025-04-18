class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        minSwap=0
        s=list(s)
        while s:
            i=s.index(s[-1])
            if i==len(s)-1:
                minSwap+=i//2
            else:
                minSwap+=i
                s.pop(i)
            s.pop()
        return minSwap
