class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left=0
        right=0
        longestSubstring=0

        while (right<len(s)):
            #if we don't have a valid window 
            while s[right] in s[left:right]:
                left+=1
            longestSubstring=max(longestSubstring,right-left+1)
            right+=1
        return longestSubstring


        
                
            


        