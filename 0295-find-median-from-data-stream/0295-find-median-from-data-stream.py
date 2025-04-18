class MedianFinder:
    def __init__(self):
        self.smallHeap=[]
        self.largeHeap=[]
        
    def addNum(self, num: int) -> None:
        if not self.largeHeap or num>self.largeHeap[0]:
            heapq.heappush(self.largeHeap,num) 
        else:
            heapq.heappush(self.smallHeap,-num) 
        if abs(len(self.largeHeap)-len(self.smallHeap))>1:
            if len(self.largeHeap)>len(self.smallHeap):
                x=heapq.heappop(self.largeHeap)
                heapq.heappush(self.smallHeap,-x) 
            else:
                x=-heapq.heappop(self.smallHeap)
                heapq.heappush(self.largeHeap,x)                 
             
    def findMedian(self) -> float:
        if len(self.smallHeap)>len(self.largeHeap):
            return -self.smallHeap[0]
        elif len(self.smallHeap)<len(self.largeHeap):
            return self.largeHeap[0]
        return (self.largeHeap[0]-self.smallHeap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()