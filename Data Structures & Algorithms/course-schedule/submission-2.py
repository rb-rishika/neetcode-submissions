class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preReq={i:[] for i in range(numCourses)}
        visiting=set()

        for course, pre in prerequisites:
            preReq[course].append(pre)

        def dfs(course):
            if course in visiting:
                #cycle detected.. 
                return False
            if preReq[course] ==[]:
                return True
            
            visiting.add(course)
            for pre in preReq[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            preReq[course]=[]
            return True
            



        for i in range(len(preReq)):
            if not dfs(i):
                return False

        return True
        