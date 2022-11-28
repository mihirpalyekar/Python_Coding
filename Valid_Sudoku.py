class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        for r in range(n):
            row = [c for c in board[r] if c != '.']
            if len(row) != len(set(row)): return False
        for c in range(n):
            row = [board[r][c] for r in range(n) if board[r][c] != '.']
            if len(row) != len(set(row)): return False
        
        def helper(r,c):
            l = set()
            for i in range(r,r+3):
                for j in range(c,c+3):
                    if board[i][j] == '.': continue
                    if board[i][j] not in l:
                        l.add(board[i][j])
                    else:
                        return False
            return True
        
        for i in range(0,n,3):
            for j in range(0,n,3):
                if not helper(i,j): return False
        return TrueV