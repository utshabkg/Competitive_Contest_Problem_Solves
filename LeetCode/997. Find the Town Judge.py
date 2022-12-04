from collections import defaultdict


class Solution:

    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if len(trust) == 0 and n == 1:
            return 1

        graph = defaultdict(list)
        trusting_people = []
        for a, b in trust:
            graph[b].append(a)
            trusting_people.append(a)
        # print(graph)

        for key in graph.keys():
            if len(graph[key]) == n - 1 and key not in trusting_people:
                return key
        return -1
