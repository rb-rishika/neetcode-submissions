class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row= len(text1)
        col= len(text2)
        lcs= dp = [[0] * (col + 1) for x in range(row + 1)]
        [[0,0,0],[0,0,0],[0,0,0],[0,0,0] ] #text1= crab, text2= cat

        for i in range(1, row+1):
            for j in range(1, col+1):
                if text1[i-1]==text2[j-1]:
                    lcs[i][j]= 1+ lcs[i-1][j-1]
                else:
                    lcs[i][j]=max(lcs[i-1][j], lcs[i][j-1])
        return lcs[row][col]
        