class Solution:
    def __init__(self):
        self.count = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 
        if root.left:
            left= self.kthSmallest(root.left,k)
            if left is not None:
                return left
        self.count+=1
        if self.count==k:
            return root.val
        if root.right:
            right= self.kthSmallest(root.right,k)
            if right is not None:
                return right


