class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums)<k:
            return 
        p = []
        for _ in nums[:k]:
            heapq.heappush(p,_)
        for x in nums[k:]:
            if x> p[0]:
                heapq.heappop(p)
                heapq.heappush(p,x)
        return p[0]
