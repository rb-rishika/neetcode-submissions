class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:


        def compute_intersect(arr1, arr2):
            intersect= set()
            for i in range(len(arr1)):
                if arr1[i] in arr2:
                    intersect.add(arr1[i])
            return list(intersect)

        len_num1= len(nums1)
        len_num2= len(nums2)

        if len_num1< len_num2:
            return compute_intersect(nums1, nums2)
        else: 
            return compute_intersect(nums2, nums1)
        