class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[0]*(len(s)+1)
        if not s or s[0] == '0':
            return 0
        #Base Case 
        dp[0], dp[1]=1,1
        for i in range(2,len(s)+1):
            digit= int(s[i-1])
            if digit!=0: #consider 111
                dp[i]+=dp[i-1]

            digit= int(s[i-2:i])
            if 10<=digit<=26:
                dp[i]+=dp[i-2]

        return dp[len(s)]

        