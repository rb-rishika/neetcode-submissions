#https://www.youtube.com/watch?v=IlEsdxuD4lY
#https://neetcode.io/problems/count-paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #m=3, n=7 
        row=[1]*n #[1,1,1,1,1,1,1]
        for i in range(m-1):
            newRow = [1]*n#[with each iteration, we compute row on top of it]
            for j in range(n-2, -1,-1):
                newRow[j]= newRow[j+1] + row[j]
            row= newRow
        return row[0]
        