class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right= len(nums)-1
        i=0 # quick sort initial partition
        #we do not shift i in case of right swap because anything can come from right 0,1,2. but only 0,1 can come from the left

        while (i<=right):
            if nums[i]==0:
                nums[left],nums[i]= nums[i], nums[left]
                left+=1
            elif nums[i]==2: 
                nums[right],nums[i]= nums[i], nums[right]
                right-=1
                i-=1
            
            i+=1
        return nums
            
            
