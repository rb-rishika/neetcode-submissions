class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack=[]

        for astr in asteroids:
            while stack and astr<0 and stack[-1]>0:
                temp=astr + stack[-1]
                if temp==0:
                    stack.pop()
                    astr=0
                elif temp > 0:
                    astr=0
                else:
                    stack.pop()

            if astr!=0:
                stack.append(astr)
        return stack



        