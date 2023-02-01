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


def solution(n:int):
    d = [0] * (n*2)

    for i in range(2, n+1):
        d[i] = d[i - 1] + 1
        if i % 2 == 0 :
            d[i] = min(d[i], d[i // 2] + 1)
        if i % 3 == 0 :
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 5 == 0 :
            d[i] = min(d[i], d[i // 5] + 1)

    print(d)


solution(44)
