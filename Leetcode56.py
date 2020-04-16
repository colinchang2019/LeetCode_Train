class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1:
            return intervals
        intervals = sorted(intervals,key=lambda x:x[0])
        res = [intervals[0]]
        for x in intervals[1:]:
            if res[-1][1]>=x[0]:
                res[-1][1] = max(x[1],res[-1][1])
            else:
                res.append(x)
        return res
