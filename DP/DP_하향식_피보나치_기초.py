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

    d = [0] * (m+1)

    def fibo(x):
        if x == 1 or x == 2 :
            return 1

        if d[x] != 0 :
            return d[x]
        d[x] = fibo(x - 1) + fibo(x - 2)
        return d[x]

    print(fibo(m))

solution(99)