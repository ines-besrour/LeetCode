class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class MyLinkedList:
    def __init__(self):
        self.length=0
        self.obj=ListNode()

    def get(self, index: int) -> int:
        if index>=self.length:
            return -1
        node=self.obj.next
        for _ in range(index):
            node=node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        head=ListNode(val,self.obj.next)
        self.obj.next=head
        self.length+=1
        
    def addAtTail(self, val: int) -> None:
        if self.length==0:
            self.addAtHead(val)
        else:
            node=self.obj.next
            while node and node.next:
                node=node.next
            node.next=ListNode(val,None)
            self.length+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self.addAtHead(val)
        elif index==self.length:
            self.addAtTail(val)
        elif index<self.length:
            node=self.obj.next
            nodeToAdd=ListNode(val)
            for _ in range(index-1):
                node=node.next
            dummy=node.next
            node.next=nodeToAdd
            nodeToAdd.next=dummy
            self.length+=1

    def deleteAtIndex(self, index: int) -> None:
        if index==0:
            self.obj=self.obj.next
            self.length-=1
        elif index<self.length:
            node=self.obj.next
            for _ in range(index-1):
                node=node.next
            node.next=node.next.next
            self.length-=1
# Your MyLinkedList self.object will be instantiated and called as such:
# self.obj = MyLinkedList()
# param_1 = self.obj.get(index)
# self.obj.addAtHead(val)
# self.obj.addAtTail(val)
# self.obj.addAtIndex(index,val)
# self.obj.deleteAtIndex(index)