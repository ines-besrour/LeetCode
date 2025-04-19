# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return 
        maxNum=max(nums)
        indexNum=nums.index(maxNum)
        root=TreeNode(maxNum)
        root.left=self.constructMaximumBinaryTree(nums[:indexNum])
        root.right=self.constructMaximumBinaryTree(nums[indexNum+1:])
        return root