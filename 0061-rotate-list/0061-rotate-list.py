# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head
        node,fast=head,ListNode(next=head)
        n=0
        while node:
            n+=1
            node=node.next
        k=k%n
        if not k:
            return head
        for _ in range(n-k):
            fast=fast.next
        top=fast.next
        dummy=top
        fast.next=None
        while top.next:
            top=top.next
        top.next=head
        return dummy
