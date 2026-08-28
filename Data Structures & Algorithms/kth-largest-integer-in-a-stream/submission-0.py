import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # parent = (i-1 )/2
        # left = 2i + 1
        # Right = 2i + 2

        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
    
    def add(self, val: int) -> int:

        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]



    