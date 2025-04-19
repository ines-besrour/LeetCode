"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        nodeCopy=Node(node.val)
        hashmap={1:nodeCopy}
        visited=set()
        def dfs(node,nodeCopy):
            visited.add(node.val)
            for neighbor in node.neighbors:
                if neighbor.val not in hashmap:
                    neighborCopy=Node(neighbor.val)
                    hashmap[neighbor.val]=neighborCopy
                else:
                    neighborCopy=hashmap[neighbor.val]
                nodeCopy.neighbors.append(neighborCopy)
                if neighbor.val not in visited:
                    dfs(neighbor,neighborCopy)
        dfs(node,nodeCopy)
        return nodeCopy