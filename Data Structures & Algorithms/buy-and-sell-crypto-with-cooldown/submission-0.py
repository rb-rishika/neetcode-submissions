class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        def dfs(i, buying):
            #Base Case- make sure it is in bounds
            if i>=len(prices):
                return 0
            if (i,buying) in dp:
                return dp[(i, buying)]
            #make a decision - buy or sell?
            if(buying):
                buyingTemp= dfs(i+1, not buying) - prices[i]
                #cooldown 
                cooldown= dfs(i+1, buying)
                dp[(i, buying)]= max(buyingTemp,cooldown)
            else:
                sellingTemp= dfs(i+2, not buying) + prices[i]
                #cooldown 
                cooldown= dfs(i+1, buying)
                dp[(i, buying)]= max(sellingTemp,cooldown)
            return dp[(i, buying)]
        
        return dfs(0, True)