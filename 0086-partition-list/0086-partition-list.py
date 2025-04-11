# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left,right=ListNode(next=head),ListNode(next=head)
        dummyLeft,dummyRight=left,right
        while head:
            if head.val<x:
                left.next=head
                left=left.next
            else:
                right.next=head
                right=right.next
            head=head.next
        right.next=None
        left.next=dummyRight.next
        return dummyLeft.next