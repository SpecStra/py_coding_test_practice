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


def solution(m):
    d = [0] * (m + 1)

    d[1] = 1
    d[2] = 1

    for i in range(3, m):
        # 뒤에 있는걸 원소로, 기록해둔걸 불러오는 방식
        d[i] = d[i - 1] + d[i - 2]

    print(d)


solution(100)
