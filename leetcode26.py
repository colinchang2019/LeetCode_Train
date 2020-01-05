# 有效地数独
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[0 for _ in range(10)] for i in range(9)] # 行的集合
        col = [[0 for _ in range(10)] for i in range(9)] # 列的集合
        blo = [[0 for _ in range(10)] for i in range(9)] # 宫的集合
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                t = int(board[i][j])
                if row[i][t]: return False
                if col[j][t]: return False
                if blo[j//3+i//3*3][t]: return False
                row[i][t] = 1
                col[j][t] = 1
                blo[j//3+i//3*3][t] = 1
        return True
