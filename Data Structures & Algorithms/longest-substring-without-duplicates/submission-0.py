class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Intuition: update the left pointer when s[l]==s[r]
        l, r=0,0
        substring=set()
        maxLen=0
        while (r<len(s)):
            while s[r] in substring:
                substring.remove(s[l])
                l+=1
            substring.add(s[r])
            maxLen= max(maxLen, r-l+1)
            r+=1
        return maxLen