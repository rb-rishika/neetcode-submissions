class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS=len(matrix), len(matrix[0])
        low=0
        high=ROWS*COLS -1
        while(low<=high):
            mid=(low+high)//2
            row, col= mid//COLS, mid%COLS
            if target==matrix[row][col]:
                return True
            elif target<matrix[row][col]:
                high=mid-1
            else:
                low=mid+1
        return False