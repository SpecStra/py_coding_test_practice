import copy
import heapq
import itertools
import re
from itertools import combinations, permutations, islice
from collections import defaultdict, OrderedDict, deque, Counter
import math
import datetime
from dateutil.relativedelta import relativedelta


def solution(grid):
    # 아이디어 : [0,0]에서 BFS를 통해 전진하면서 방문한 경우 cnt를 해당 원소로 바꾼다. 방문하는 곳은 1인곳만
    n, m = len(grid[0]), len(grid)
    graph = grid
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    if grid[m - 2][n - 1] == 0 and grid[m - 1][n - 2] == 0:
        return -1

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                # print(nx, ny)
                if graph[nx][ny] == 0:
                    continue

                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
        return graph[m - 1][n - 1]

    ans = bfs(0, 0)

    # for check
    for z in graph:
        print(z)

    return ans if ans != 1 else -1


a = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
b = [
    [1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 1],
]
c = [
    [1, 0],
    [0, 1]
]
solution(b)

# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 알고리즘은 진즉에 제대로 갖다 썼는데 입구가 막혀있는 경우랑 출구가 막혀있는 경우 조건문 짜다가 시간 다버렸다.
# 결국 출구 막힌 경우는 len관련해서 틀어막고, 출구가 막혀있는 경우 = 답이 1이 나오는 것을 이용해서 1인 경우 걍 -1로 반환처리
# DFS때도 그렇지만 index out 조건문이랑 0인경우 조건문은 서로 분리해두는 편이 낫겠다. 괜히 IndexError 나면 안되니까.
