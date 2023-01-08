import copy
import heapq
import itertools
import re
from itertools import combinations, permutations, islice
from collections import defaultdict, OrderedDict, deque, Counter
import math
import datetime
from dateutil.relativedelta import relativedelta


def solution(sizes):
    width = []
    height = []
    for i in range (len(sizes)):
        width.append(max(sizes[i]))
        height.append(min(sizes[i]))
    print(width, height)
    answer=max(width)*max(height)
    print(answer)
    return answer


solution([[60, 50], [30, 70], [60, 30], [80, 40]])

# https://school.programmers.co.kr/learn/courses/30/lessons/86491
# 핵심은 sizes에 주어지는 가로, 세로는 상관 없이 '[큰놈, 작은놈]'으로 만든 다음 max(큰놈), max(작은놈) 하는 것.
# 지갑, 길이 등 생소한 단어에 매달리면 피를 본다. 분류는 완전탐색이였지만, 단순한 구현으로 해결할 수 있는 모양.
