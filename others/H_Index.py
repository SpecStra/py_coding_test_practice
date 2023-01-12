import copy
import heapq
import itertools
import re
from itertools import combinations, permutations, islice
from collections import defaultdict, OrderedDict, deque, Counter
import math
import datetime
from dateutil.relativedelta import relativedelta


def solution(citations):
    sc = sorted(citations, reverse=True)
    print(sc)
    for i in range(len(sc)):
        print(i+1, sc[i])
        if i+1 == sc[i]:
            return i+1
        elif i+1 > sc[i]:
            return i
        if len(sc) == i+1:
            return i+1


a = [3, 0, 6, 1, 5]
b = [15, 12, 10, 8, 6, 3, 2, 1]
c = [10, 10, 10, 10, 10]
solution(c)

# https://school.programmers.co.kr/learn/courses/30/lessons/42747
# 그냥 공식 알면 풀고 모르면 한참 헤메는 문제. 이게 뭔 정렬문제야..
