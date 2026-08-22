class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=set()
        visited=[False]*len(nums)
        def dfs(index, curr):
            if index==len(nums):
                res.add(tuple(curr.copy()))
                return
            for i in range(len(nums)):
                if visited[i]==True:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                print(index, curr)
                visited[i]= True
                curr.append(nums[i])
                dfs(index+1, curr)
                curr.pop()
                visited[i]= False                

        dfs(0,[])
        return [list(r) for r in res]