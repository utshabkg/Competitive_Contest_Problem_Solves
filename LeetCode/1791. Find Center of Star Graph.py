class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        for i in range(len(edges)):
            first = edges[i][0]
            second = edges[i][1]

            if first in edges[i + 1]:
                center = first
            else:
                center = second
            break

        return center