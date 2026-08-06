class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res=2*len(nums)*[0]
        for i in range(len(nums)):
            print(len(nums))
            res[i]=nums[i]
            res[len(nums)+i]= nums[i]
        print(res)
        return res
        