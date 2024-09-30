class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O':
                    visited = set()
                    stack = []
                    stack.append((i, j))
                    while stack:
                        (poped_x, poped_y) = stack.pop()
                        visited.add((poped_x, poped_y))
                        if poped_x <= 0 or poped_x >= len(board)-1 or poped_y <= 0 or poped_y >= len(board[0])-1:
                            visited.clear()
                            break
                        for (x, y) in [
                            (poped_x + 1, poped_y),
                            (poped_x - 1, poped_y),
                            (poped_x, poped_y + 1),
                            (poped_x, poped_y - 1)]:
                            if (x, y) not in visited and board[x][y] == 'O':
                                stack.append((x, y))

                    for (x, y) in visited:
                        board[x][y] = 'X'