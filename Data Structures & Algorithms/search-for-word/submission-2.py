class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COL= len(board), len(board[0])

        def dfs(r,c,i):
            #found word
            if i==len(word):
                return True

            #checking bounds
            if (r<0 or c<0 or r >= ROWS or c >= COL or board[r][c]!=word[i]):
                return False

            temp=board[r][c] #store the value of currect board char
            board[r][c]="#"

            res = (dfs(r+1,c, i+1) or 
                    dfs(r,c+1, i+1) or 
                    dfs(r,c-1, i+1) or
                    dfs(r-1,c, i+1))
            board[r][c]= temp #you wanna replace back the "#"
            return res
            

        for i in range(ROWS):
            for j in range(COL):
                #if element== chaacter of the string we are tyring to choose
                if dfs(i,j,0):
                    return True
        return False
        

        