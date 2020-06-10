class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints)>1440:
            return 0
        for i,x in enumerate(timePoints):
            a,b = x.split(":")
            x = int(a)*60 + int(b)
            timePoints[i] = x
        timePoints.sort()
        timePoints.append(timePoints[0])
        res = 1440
        for i in range(len(timePoints)-1):
            d = abs(timePoints[i]-timePoints[i+1])
            if d>720:
                d = 1440 - d
            res = min(res,d)    
        return res
