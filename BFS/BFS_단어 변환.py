import copy
import heapq
import itertools
import re
from itertools import combinations, permutations, islice
from collections import defaultdict, OrderedDict, deque, Counter
import math
import datetime
from dateutil.relativedelta import relativedelta


def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [False] * len(words)

    queue = deque([(begin, 0)])

    begin_len = len(begin)
    words_len = len(words)
    answer = float("inf")

    while queue:
        current, cnt = queue.popleft()
        if current == target:
            answer = min(answer, cnt)
        for j in range(words_len):
            count = 0
            for i in range(begin_len):
                if words[j][i] != current[i]:
                    count += 1
            if count == 1 and not visited[j]:
                visited[j] = True
                queue.append((words[j], cnt + 1))

    return answer


a = ["hot", "dot", "dog", "lot", "log", "cog"]
solution("hit", "cog", a)

# https://school.programmers.co.kr/learn/courses/30/lessons/43163
# BFS문제. 어쨰 DFS랑 BFS는 풀이방법의 90%가 다 비슷하고 구현할건 10%밖에 없는 것 같다.
# -> 즉 BFS/DFS로 될 것 같다는걸 알기만 하면 거저먹을 수 있다는 뜻.
