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


def solution(x, y, n):
    d = [1000] * x + [0] * ((y - x)+1)
    d[x] = 0

    for i in range(x+1, y+1):
        if i - n < 0:
            continue
        d[i] = d[i - n] + 1
        if i % 2 == 0:
            d[i] = min(d[i], d[int(i / 2)] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[int(i / 3)] + 1)
        print(d)

    if d[y] > 1000:
        return -1
    else :
        return d[y]


solution(1, 30, 1)
# solution(2, 5, 4)

# https://school.programmers.co.kr/learn/courses/30/lessons/154538