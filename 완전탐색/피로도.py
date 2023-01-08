import copy
import heapq
import itertools
import re
from itertools import combinations, permutations, islice
from collections import defaultdict, OrderedDict, deque, Counter
import math
import datetime
from dateutil.relativedelta import relativedelta


def solution(k, dungeons):
    ans = []
    lens = [i for i in range(0, len(dungeons))]
    for i in list(permutations(lens)):
        priodo = copy.deepcopy(k)
        cnt = 0
        for index, j in enumerate(i):
            current_dun = dungeons[j]
            if current_dun[0] > priodo:
                ans.append(cnt)
                break
            else:
                priodo -= current_dun[1]
                cnt += 1
                if index+1 == len(i):
                    ans.append(cnt)

    return max(ans)


solution(80, [[80, 20], [50, 40], [30, 10]])


# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 완전탐색으로 안 풀면 피를 볼 것 같은 문제. 제한사항에서 던전이 8개밖에 안되는걸 보고 완전탐색으로 해버려야지~ 하는게 풀이방법인 것 같다.
# DFS로 풀기도 하던데, 난 그냥 순열로 순서 나열해서 풀었다.
