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

# 선형 배열에서 가장 먼저 생략된 생략된 양의 정수를 찾으세요
def solution(n: list):
    n.sort()
    print(list(filter(lambda x: x + 1 not in n and x > 0, n))[0] + 1)
    return list(filter(lambda x: x + 1 not in n and x > 0, n))[0] + 1

def solution2(n: list):
    a = set(n)
    i = 1
    while i in a:
        i += 1
    print(i)
    return i

# solution([3, 4, -1, 1])
# solution([1, 2, 0])

solution2([3, 4, -1, 1])
solution2([1, 2, 0])

# 접근 : 자신+1이 배열에 있는지 sort된 리스트를 필터링해서 return한다. 음수와 0은 x > 0으로 걸러낸다.
