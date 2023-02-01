import copy
import heapq
import itertools
import re
from itertools import combinations, permutations, islice
from collections import defaultdict, OrderedDict, deque, Counter
import math
import datetime
from dateutil.relativedelta import relativedelta
from functools import reduce


def solution(n: int, m: list):
    d = [10001] * n
    d[0] = 0

    for i in range(len(m)):
        for j in range(m[i], n + 1): # j 시작은 1개 화폐로 만들 수 있는 지점인 m[i]가 2:, 3:, 5:
            print(f"i:{i}, j:{j} part")
            if d[j - m[i]] != 10001 : # (i - k)원을 만드는 방법이 존재하는 경우
                d[j] = min(d[j], d[j - m[i]] + 1)

    print(d)


# solution(7, [2, 3, 5])
solution(4, [3, 5, 7])
