class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #recuur= dp[i]= d[diff]+1
        coins.sort()
        dp=[0]*(amount+1)
        
        for i in range(1, amount+1):
            minCoin=float('inf')
            #[0,1,2,3]
            for coin in coins:
                #[1,5,10]
                diff= i-coin
                if diff<0:
                    break
                minCoin= min(minCoin,1+dp[diff])
            dp[i]= minCoin
        if dp[amount]<float('inf'):
            return dp[amount]
        else:
            return -1



        
        