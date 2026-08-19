class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n<=2:
            return n
        else:
            first=1
            second =1
            for i in range(n-1):
                third=first+second
                first=second
                second=third
            return second


        # def dfs(stair):
        #     if stair==n: #we found one valid way
        #         return 1
        #     if stair>n:
        #         return 0
        #     return dfs(stair+1)+dfs(stair+2)
        

        # return dfs(0)
     