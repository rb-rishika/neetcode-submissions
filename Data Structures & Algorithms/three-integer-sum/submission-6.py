class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        left=0
        right=len(nums)-1
        sorted_nums=sorted(nums)
        output=[]

        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            if i>0 and sorted_nums[i]== sorted_nums[i-1]:
                continue

            while left<right: 
                temp=sorted_nums[left]+sorted_nums[right]+ sorted_nums[i]

                if temp<0:
                    left+=1
                elif temp> 0:
                    right-=1
                else:
                    output.append([sorted_nums[left],sorted_nums[right],sorted_nums[i]])
                    left+=1
                    right-=1

                    while left<right and sorted_nums[left]==sorted_nums[left-1]:
                        left+=1
                    while left<right and sorted_nums[right]==sorted_nums[right+1]:
                        right-=1
        return output





            
        