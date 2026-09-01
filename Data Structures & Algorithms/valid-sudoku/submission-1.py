class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for y in range(9):
            for x in range(9):
                if board[y][x] == ".":
                    continue    
                if (board[y][x] in rows[y] or 
                    board[y][x] in cols[x] or 
                    board[y][x] in squares[(y//3, x//3)]):
                    return False
                cols[x].add(board[y][x])
                rows[y].add(board[y][x])
                squares[(y//3, x//3)].add(board[y][x])
        return True
