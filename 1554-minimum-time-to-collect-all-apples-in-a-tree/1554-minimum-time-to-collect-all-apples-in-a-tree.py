class Solution:
    def populate(self, edges: List[List[int]]):
        graph=defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        return graph

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph=self.populate(edges)
        def dfs(node,par):
            time=0
            for neighbor in graph[node]:
                if neighbor!=par:
                    childTime=dfs(neighbor,node)
                    if hasApple[neighbor] or childTime:
                        time+=2+childTime
            return time
        return dfs(0,-1)