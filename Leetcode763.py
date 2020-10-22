class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        intervals,d = [],{}
        for i,x in enumerate(S):
            if x not in d:
                intervals.append([i, S.rfind(x)])
                d[x] = i
        res = [intervals[0]]
        for x in intervals[1:]:
            if res[-1][1]>=x[0]:
                res[-1][1] = max(x[1],res[-1][1])
            else:
                res.append(x)
        return [x[1]-x[0]+1 for x in res]
        
