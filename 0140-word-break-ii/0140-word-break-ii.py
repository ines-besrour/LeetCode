class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        sentences=[]
        def helper(left,right,sentence:list):
            if right>=len(s):
                if s[left:right] in wordDict:
                    sentence.append(s[left:right])
                    sentences.append(' '.join(sentence))
                    sentence.pop()
                return
            if s[left:right+1] in wordDict:
                sentence.append(s[left:right+1])
                helper(right+1,right+1,sentence)
                sentence.pop()
            helper(left,right+1,sentence)
        helper(0,0,[])
        return sentences