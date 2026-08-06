class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows= len(word1)
        cols= len(word2)
        dp=[[0 for i in range(cols+1)] for j in range(rows+1) ]

        for i in range(rows + 1):
            dp[i][0] = i  # cost of deleting i characters from word1

        for j in range(cols + 1):
            dp[0][j] = j  # cost of inserting j characters to match word2

        for i in range(1,rows+1):
            print(i)
            for j in range(1,cols+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]= dp[i-1][j-1]
                else:
                    dp[i][j]= 1+min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
        return dp[rows][cols]

        