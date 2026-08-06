class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        #Empty tree is a valid tree
        if not edges or n==0:
            return True

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit=set()
        def dfs(curr, prev):
            if curr in visit:
                return False
            visit.add(curr)
            for nei in adj[curr]:
                if nei==prev:
                    continue
                if not dfs(nei,curr ):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n




        