import collections
import copy


def solution(graph):
    current_graph = copy.deepcopy(graph)

    def dfs_rec(v, discovered=[]):
        discovered.append(v)
        for i in current_graph[v]:
            if i not in discovered:
                discovered = dfs_rec(i, discovered)
        return discovered

    return dfs_rec(1)


a = []
sample_graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}
print(solution(sample_graph))
