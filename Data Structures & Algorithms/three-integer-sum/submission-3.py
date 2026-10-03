class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        left=0
        right=len(nums)-1
        sorted_nums=sorted(nums)
        output=[]

        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1

            while left<right: 
                temp=sorted_nums[left]+sorted_nums[right]+ sorted_nums[i]

                if temp<0:
                    left+=1
                elif temp> 0:
                    right-=1
                else: 
                    new_pair= (sorted_nums[left],sorted_nums[right], sorted_nums[i])
                    if new_pair not in output:
                        output.append(new_pair)
                    left+=1
                    right-=1
        return output





            
        