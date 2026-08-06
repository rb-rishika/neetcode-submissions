
from collections import Counter
class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict=defaultdict(list)
        for i in strs:
            count=[0]*26
            for c in i:
                count[ord(c)-ord("a")]+=1
            key= tuple(count)
            anagrams_dict[key].append(i)
        return anagrams_dict.values()