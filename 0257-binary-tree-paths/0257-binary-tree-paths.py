# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.paths=[]
        def dfs(node,path):
            if not node:
                return
            if not node.left and not node.right:
                path.append(str(node.val))
                self.paths.append('->'.join(path))
                return
            path.append(str(node.val))
            if node.left:
                dfs(node.left,path)
                path.pop()
            if node.right:
                dfs(node.right,path)
                path.pop()
                
        dfs(root,[])
        return self.paths