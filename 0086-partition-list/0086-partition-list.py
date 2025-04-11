# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy=ListNode(next=head)
        node=head
        less_x,greater_x=[],[]
        while node:
            if node.val<x:
                less_x.append(node.val)
            else:
                greater_x.append(node.val)
            node=node.next
        for l in less_x:
            head.val=l
            head=head.next
        for g in greater_x:
            head.val=g
            head=head.next
        return dummy.next