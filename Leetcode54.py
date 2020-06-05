class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        a = []
        while matrix:
            a += matrix.pop(0)
            if matrix:
                matrix = list(map(list,zip(*matrix)))[::-1]
        return a
        
