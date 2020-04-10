class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)<=2:
            return True
        d1,d2 = coordinates[0],coordinates[1]
        for i in coordinates[2:]:
            if not (i[1]-d1[1])*(d2[0]-d1[0])==(i[0]-d1[0])*(d2[1]-d1[1]):
                return False
        return True
