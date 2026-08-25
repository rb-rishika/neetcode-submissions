class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        maxFreq=0
        res=0
        hashSet={}

        #we shrink the window until it is valid. Update the best length as I go maxFreq does not need to represent the current window exactly. It represents the best frequency we’ve seen while expanding. A stale value may let the current window remain technically invalid, but it cannot cause us to discover an impossible larger answer.

        #the idea is we try to compute the max freq of a character and then see if we get a better one.

        while(right<len(s)):
            hashSet[s[right]]= hashSet.get(s[right],0) +1
            maxFreq= max(maxFreq,hashSet[s[right]] )

            while ((right-left+1)- maxFreq)>k:
                hashSet[s[left]]-=1
                left+=1
            
            res= max(res,right-left+1 )
            right+=1
        return res



        