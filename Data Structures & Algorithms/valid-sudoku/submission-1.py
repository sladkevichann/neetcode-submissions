class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 2nd solution - bitmasking!!!!!
        cols = [0] * 9 # since 1-9
        rows = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                val = int(board[r][c]) - 1
                mask = 1 << val # hardest part

                if (mask & rows[r] != 0 
                or mask & cols[c] != 0
                or mask & squares[(r // 3) * 3 + (c // 3)] != 0): #бля умом россию не понятьь
                    return False

                cols[c] |= mask
                rows[r] |= mask # OR (добавка)
                squares[(r // 3) * 3 + (c // 3)] |= mask
        return True

        