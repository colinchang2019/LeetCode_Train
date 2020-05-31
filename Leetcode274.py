class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations,reverse=True)
        res = 0
        for i,x in enumerate(citations):
            if x>=(i+1): res = i+1
            else: break
        return res
