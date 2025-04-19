class TrieNode:  
    def __init__(self):      
        self.children = [None] * 26
        self.isEndOfWord = False

class WordDictionary:
    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        node=self.root
        for c in word:
            idx=ord(c)-ord('a')
            if not node.children[idx]:
                node.children[idx]=TrieNode()
            node=node.children[idx]
        node.isEndOfWord=True

    def search(self, word: str) -> bool:
        node=self.root
        def dfs(j,node):
            for i in range(j,len(word)):
                c=word[i]
                if c=='.':
                    for child in node.children:
                        if child and dfs(i+1,child):
                            return True
                    return False
                idx=ord(c)-ord('a')
                if not node.children[idx]:
                    return False
                node=node.children[idx]
            return node.isEndOfWord

        return dfs(0,node)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)