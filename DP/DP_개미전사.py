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


# 리스트 내에서 인덱스가 서로 인접하지 않은 원소들만을 선택하여 해당 원소들로 만들 수 있는 최대값을 구하라
def solution(m: list):
    d = [0] * len(m)

    d[0] = m[0]
    d[1] = max(m[0], m[1])

    # 메모리제이션의 방식을 항상 기억할 것.
    for i in range(2, len(m)):
        d[i] = max(d[i - 1], d[i - 2] + m[i])

    print(d)


solution([1, 3, 1, 5, 6, 7, 8, 5, 4])
solution([1, 2, 99, 1, 1, 1, 1, 1])
