from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for word in strs:
            hashChars=[0]*26
            for c in word:
                hashChars[ord(c)-ord("a")]+=1
            key=tuple(hashChars)
            res[key].append(word)
        return res.values()

        