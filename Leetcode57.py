class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        res = []
        if newInterval[1]<intervals[0][0]:
            return [newInterval]+intervals
        elif newInterval[0]>intervals[-1][1]:
            return intervals+[newInterval]
        for i,x in enumerate(intervals):
            if x[-1]<newInterval[0]:
                res.append(x)
            else:
                break
        if x[0]<=newInterval[1]:
            t = [[min(x[0],newInterval[0]),max(x[1],newInterval[1])]]
        else:
            t = [newInterval,x]
        res += t
        intervals = intervals[i+1:]
        for i,x in enumerate(intervals):
            if x[0]<=res[-1][1]:
                res[-1][1] = max(res[-1][1],x[1])
            else:
                res.append(x)
        return res
