class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs={i:[] for i in range(numCourses)} #empty list to each

        for course, pre in prerequisites:
            prereqs[course].append(pre)
        print(prereqs)

        visited=set()
        def dfs(currCourse):
            #cycle detected
            if currCourse in visited:
                return False
            #course can be completed
            if prereqs[currCourse]==[]:
                return True
            visited.add(currCourse)

            for pre in prereqs[currCourse]:
                if not dfs(pre):
                    return False
            visited.remove(currCourse)
            return True

        for currCourse in range(numCourses):
            print(currCourse)
            if not dfs(currCourse):
                return False

        return True








        