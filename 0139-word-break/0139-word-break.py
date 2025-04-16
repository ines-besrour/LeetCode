class Solution:
    def __init__(self):
        self.memo={}
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)  
        return self._dfs(s, wordSet)

    def _dfs(self, s: str, wordSet: set) -> bool:
        if s in self.memo:
            return self.memo[s]
        if not s:
            return True

        for i in range(1, len(s)+1):
            if s[:i] in wordSet and self._dfs(s[i:], wordSet):
                self.memo[s] = True
                return True

        self.memo[s] = False
        return False