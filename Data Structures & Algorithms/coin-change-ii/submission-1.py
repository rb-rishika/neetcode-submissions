class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i, curr_sum):
    # Base Case
            if curr_sum == amount:
                return 1
            if curr_sum > amount or i == len(coins):
                return 0
            if (i, curr_sum) in dp:
                return dp[(i, curr_sum)]
    
    # Two choices:
    # 1. Pick the coin (stay at same i)
    # 2. Don't pick the coin (move to i+1)
            dp[(i, curr_sum)] = dfs(i, curr_sum + coins[i]) + dfs(i + 1, curr_sum)
    
            return dp[(i, curr_sum)]

        return dfs(0, 0)