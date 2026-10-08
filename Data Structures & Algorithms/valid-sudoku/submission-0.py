class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        def getBox(i, j):
            return (i // 3) * 3 + j // 3

        for r in range(9):
            for c in range(9):

                val = board[r][c]

                if val == '.': continue

                if (val in rows[r] 
                    or val in cols[c] 
                    or val in boxes[getBox(r,c)]):
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[getBox(r,c)].add(val)

        return True
