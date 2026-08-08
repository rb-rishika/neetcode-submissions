class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        longest_substring=set()
        length=0
        maxLength=0

        while right<len(s):
            while s[right] in longest_substring:
                longest_substring.remove(s[left])
                left+=1
            longest_substring.add(s[right])
            maxLength=max(maxLength, right-left+1)
            right+=1
        print(longest_substring)
        return maxLength
                
            


        