import copy
import heapq
import itertools
import re
from itertools import combinations, permutations, islice
from collections import defaultdict, OrderedDict, deque, Counter
import math


def solution(s):
    qu = deque()
    for index, i in enumerate(list(s)):
        if index == 0:
            qu.append(i)
            print(qu)
            continue
        else :
            qu.append(i)
            if len(qu) > 1 and qu[-1] == qu[-2]:
                qu.pop()
                qu.pop()
    if len(qu) > 0:
        return 0
    else:
        return 1

a = "baabaa"
solution(a)

# https://school.programmers.co.kr/learn/courses/30/lessons/12973
# pop부분에 while을 써야될지 모르겠어서 일단 돌려봤는데 바로 100점나옴..
