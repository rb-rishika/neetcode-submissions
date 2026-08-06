from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            prereqs[course].append(pre)

        visited = set()
        visiting = set()
        result = []

        def dfs(course):
            if course in visiting:  # Cycle detected
                return False
            if course in visited:   # Already processed
                return True

            visiting.add(course)
            for pre in prereqs[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            visited.add(course)
            result.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return result