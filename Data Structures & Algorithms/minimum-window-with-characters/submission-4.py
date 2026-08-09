from collections import Counter

#s = "OUZODYX AZV", t = "XYZ"
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        elem_t= Counter(t)
        elem_s= defaultdict(int)
        need=len(elem_t)
        have=0
        minLength=float('inf')
        left= 0
        res=[-1,-1]

        if len(t)>len(s): return ""

        for right in range(len(s)):
            elem_s[s[right]]+=1
            if s[right] in elem_t and elem_s[s[right]]==elem_t[s[right]]:
                have+=1
            while need==have:
                #if window <minLenght
                if (right-left+1) < minLength:
                    minLength=right-left+1
                    res=[left,right]
                    
                #we need to remove from elem_s and have.. 
                elem_s[s[left]]-=1

                #did we make the window invalid??
                if s[left] in elem_t and elem_s[s[left]]<elem_t[s[left]]:
                    have-=1
                left+=1

        l,r= res
                
        return s[l: r+1]


#Brute Force, time limit
        # counter_t= Counter(t)
        # minLength= float("inf")
        # res=""
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         substring_temp=s[i:j+1]
        #         window= Counter(substring_temp)
        #         valid= True
        #         for c in counter_t:
        #             if window[c]< counter_t[c]:
        #                 valid=False
        #         if valid and len(substring_temp)< minLength:
        #             minLength=len(substring_temp)
        #             res=substring_temp
        # return res
        #Optimized Brute Force : we just make sure tto not construct a new substring every j loop
        # counter_t= Counter(t)
        # minLength= float("inf")
        # res=""
        # for i in range(len(s)):
        #     window=defaultdict(int)
        #     for j in range(i,len(s)):
        #         window[s[j]]+=1
                
        #         valid= True
        #         for c in counter_t:
        #             if window[c]< counter_t[c]:
        #                 valid=False
        #         if valid and j-i+1< minLength:
        #             minLength=j-i+1
        #             res=s[i:j+1]
        # return res












        
        