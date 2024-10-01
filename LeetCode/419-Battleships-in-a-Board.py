class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        def dfs(i, j):
            board[i][j] = '.'
            for (ii, jj) in [
                (i-1, j),
                (i+1, j),
                (i, j-1),
                (i, j+1)]:
                if 0 <= ii < len(board) and 0 <= jj < len(board[ii]) and board[ii][jj] == 'X':
                    dfs(ii, jj)
            
        count = 0

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    count += 1
                    dfs(i, j)
        
        return count
        