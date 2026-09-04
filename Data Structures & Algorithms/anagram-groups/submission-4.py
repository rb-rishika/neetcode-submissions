class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        dict_anagrams={}
        for i in strs:    #act
            key=[0]*26
            for c in (i):
                key[ord(c)- ord("a")]+=1
            if (tuple(key)) in dict_anagrams:
                dict_anagrams[tuple(key)].append(i)
            else: 
                dict_anagrams[(tuple(key))]=[i]

        return list(dict_anagrams.values())
        
        
                