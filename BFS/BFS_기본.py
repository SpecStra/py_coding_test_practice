import copy
import heapq
import itertools
import re
from itertools import combinations, permutations, islice
from collections import defaultdict, OrderedDict, deque, Counter
import math
import datetime
from dateutil.relativedelta import relativedelta


def solution(graph):
    visited = [False] * len(graph)

    queue = deque([(graph[0], 0)])

    while queue:
        item, cnt = queue.popleft()
        print(item, cnt)
        for i in item:
            if not visited[i - 1]:
                visited[i - 1] = True
                queue.append((graph[i - 1], cnt + 1))


g = [
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
solution(g)


# 함수형이 아닌 기본 while형태
