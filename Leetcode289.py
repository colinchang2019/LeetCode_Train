class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n,m = len(board),len(board[0])
        sit = [[0 for _ in range(m)] for j in range(n)]
        dire = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        n,m = len(board),len(board[0])
        for i in range(n):
            for j in range(m):
                count = 0
                sit[i][j] = board[i][j]
                for x,y in dire:
                    xn = i+x
                    yn = j+y
                    if 0<=xn<n and 0<=yn<m and board[xn][yn]==1:
                        count += 1
                        #if i==0 and j==2:print((i,j),count)
                #　print((i,j),count)
                if count<2 or count>3:
                    sit[i][j] = 0
                elif count==3:
                    sit[i][j] = 1
                else: continue
        for i in range(n):
            for j in range(m):
                board[i][j] = sit[i][j]
