class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_row = [set() for _ in range(9)] # Creating 9 sets for each row, _ is a throwaway variable
        valid_col = [set() for _ in range(9)] # Creating 9 sets for each col, _ is a throwaway variable
        valid_box = [set() for _ in range(9)] # Creating 9 sets for each box, _ is a throwaway variable
     
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                box_index = (i // 3) * 3 + (j // 3) 
                # Maps (row, col) -> box number 0-8. i//3 and j//3 give the row-band/col-band (0,1,2 each).
                # Multiply row-band by 3 to spread the 3 row-bands into non-overlapping ranges (0-2, 3-5, 6-8),
                # then col-band picks which of the 3 boxes within that range. Same idea as reading a 3x3 grid:
                # jumping down one row of boxes = +3, jumping across one column of boxes = +1.
                if val == ".":
                    continue   # Skip empty cells, nothing to check
                # Otherwise, val is a digit like "5" — check it against the right trackers
                if val in valid_row[i] or val in valid_col[j] or val in valid_box[box_index]: # If it's been seen before in this specific row/col/box
                    return False
                else:
                    valid_row[i].add(val) # Add the number to the hash set
                    valid_col[j].add(val)
                    valid_box[box_index].add(val) 
       
        return True