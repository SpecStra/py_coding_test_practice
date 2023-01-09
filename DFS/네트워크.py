import copy
import heapq
import itertools
import re
from itertools import combinations, permutations, islice
from collections import defaultdict, OrderedDict, deque, Counter
import math
import datetime
from dateutil.relativedelta import relativedelta


def solution1(n: int, computers):
    connection = []
    n_range = list(range(n))
    for i in range(n):
        for j in range(n):
            if i != j:
                if computers[i][j] == 1 and computers[j][i] == 1:
                    if i in n_range:
                        n_range.remove(i)
                    elif j in n_range:
                        n_range.remove(j)

                    if sorted((i, j)) not in connection:
                        if not connection:
                            connection.append(sorted((i, j)))
                        else:
                            for index, z in enumerate(connection):
                                if i in z and j in z:
                                    break
                                if i in z:
                                    connection[index].append(j)
                                    break
                                elif j in z:
                                    connection[index].append(i)
                                    break
                                else:
                                    # print(i,j, index, len(connection) - 1)
                                    if index == len(connection) - 1:
                                        connection.append(sorted((i, j)))
    # print(connection, n_range)
    dupl = []
    # i, j가 각각의 배열에 있어서 구분 되지 못 한 것을 찾아줍니다.
    for i in range(len(connection)):
        for j in connection[i]:
            dupl.append(j)

    # 필터링을 통해 합쳐줍시다.
    for i in Counter(dupl).most_common():
        if i[1] > 1:
            vanish = list(filter(lambda x:i[0] in x, connection))
            connection = list(filter(lambda x:i[0] not in x, connection))
            mute = []
            for j in range(len(vanish)):
                mute += vanish[j]
                if j != len(vanish) -1:
                    mute.remove(i[0])
            connection.append(mute)
    # print(len(connection) + len(n_range))
    return len(connection) + len(n_range)


def solution2(n:int, computers):
    connection = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                if j not in connection[i]:
                    connection[i].append(j)

    visited = [False for i in range(n)]

    stack = []
    def dfs(graph, v, visited):
        visited[v] = True
        print(v, end="")
        for i in graph[v]:
            if not visited[i]:
                dfs(graph, i, visited)

    dfs(connection, 1, visited)
    print(connection)
    print(stack)




a = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

b = [
    [1, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 0, 1]
]

c = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

c1 = [
    [1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 1]
]
solution2(4, b)
"""
print(solution2(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)
print(solution2(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]), 1)
print(solution2(3, [[1, 0, 1], [0, 1, 0], [1, 0, 1]]), 2)
print(solution2(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]), 1)
print(solution2(4, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]), 4)
"""

# https://school.programmers.co.kr/learn/courses/30/lessons/43162
# 내가 푼 것이 sol1. 최대 배열 크기가 200x200이라 충분이 단순 연산으로 될 것 같아서 연산으로 풀어봤다.
# 테케에서 3번 빠꾸먹고 4번째에 통과. 1시간정도 걸린듯.
# BFS나 DFS를 이용한 sol2 : 작성중.. 이해 되는대로 수정 예정
