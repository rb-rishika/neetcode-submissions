class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                break
            elif i>0 and nums[i]==nums[i-1]:
                continue
            low=i+1
            high=len(nums)-1
            while(low<high):
               
                tmp= nums[i]+nums[low]+nums[high]
                print(nums[i],nums[low],nums[high])
                if tmp==0: #if three ints sum
                    result.append([nums[i],nums[low],nums[high]])
                    low+=1
                    high-=1
                    #[-2,-2,0,0,2,2]
                    while low<high and nums[low]==nums[low-1]:
                        low+=1
                    while low<high and nums[high]==nums[high+1]:
                        high-=1
                else:
                    if tmp>0:
                        high-=1
                    else:
                        low+=1
        return result

