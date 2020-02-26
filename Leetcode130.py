from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])

        for j in range(col):
            # 第一行
            if board[0][j] == "O":
                self.bfs(0, j,board,row,col)
            # 最后一行
            if board[row - 1][j] == "O":
                self.bfs(row - 1, j,board,row,col)

        for i in range(row):
            if board[i][0] == "O":
                self.bfs(i, 0,board,row,col)
            if board[i][col - 1] == "O":
                self.bfs(i, col - 1,board,row,col)

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "B":
                    board[i][j] = "O"

    def bfs(self,i,j,board,n,m):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        p = deque()
        p.appendleft((i,j))
        while p:
            i,j = p.pop()
            if 0<=i<n and 0<=j<m and board[i][j]=='O':
                board[i][j] = 'B'
                for d in directions:
                    xp,yp = i+d[0],j+d[1]
                    p.appendleft((xp,yp))
