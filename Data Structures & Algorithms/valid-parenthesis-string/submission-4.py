class Solution:
    def checkValidString(self, s: str) -> bool:
        left=[]
        star=[]

        for i, ch in enumerate(s):
            if ch=="(":
                left.append(i)
            elif ch=="*":
                star.append(i)
            else:
                if not left and not star:
                    return False
                if left:
                    left.pop()
                else:
                    star.pop()
        #taking care of remaining lefts and using star
        #as closing brackets
        while left and star:
            #star appears before opening "("
            if star.pop()<left.pop():
                return False
        print(left)
        return not left

            