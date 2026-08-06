class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns= collections.defaultdict(set)
        rows= collections.defaultdict(set)
        squares= collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                if ((board[r][c] in rows[r]) or (board[r][c] in columns[c]) or (board[r][c] in squares[(r//3,c//3)])):
                    return False
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        print(squares)
        '''
        defaultdict(
<
class
'set'
>
, {(0, 0): {'4', '9', '1', '8', '2'}, (0, 1): {'3', '5'}, (0, 2): {'3'}, (1, 0): {'5', '7'}, (1, 1): {'3', '6', '8', '2'}, (1, 2): {'6', '4', '5'}, (2, 2): {'9', '8', '2', '7'}, (2, 1): {'8', '1', '4', '9'}})
        '''
        return True
