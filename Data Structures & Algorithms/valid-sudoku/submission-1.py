class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set) # Defaultdict(set) allows us to create a dict without a key, automatically assigning a (set) as the value even if the key is missing
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) # Key = (r / 3, c / 3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".": # Empty cells can be skipped as it can't be a dupe
                    continue
                if (val in rows[r] or
                    val in cols[c] or
                    val in squares[(r // 3, c // 3)]):
                    return False
                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)
       
        return True