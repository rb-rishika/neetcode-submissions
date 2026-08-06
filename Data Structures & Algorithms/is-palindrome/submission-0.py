class Solution:
    def isPalindrome(self, s: str) -> bool:
        updatedStr= s.replace(" ", "")
        low=0
        high=len(updatedStr)-1
        while low<high:
            print(updatedStr[high].isalnum())
            while low<high and not updatedStr[low].isalnum():
                low+=1
            while low<high and not updatedStr[high].isalnum():
                high-=1
            if (updatedStr[low].lower()!=updatedStr[high].lower()):
                return False
            else:
                low+=1 
                high-=1
        return True        