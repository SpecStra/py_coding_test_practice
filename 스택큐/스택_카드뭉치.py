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


def solution(cards1:list, cards2:list, goal:list):
    stack = []
    one_next = 0
    two_next = 0
    while len(stack) != len(goal):
        poped = goal.pop(0)
        if poped in cards1:
            i = cards1.index(poped)
            if i == one_next:
                one_next += 1
            else:
                return "No"
        elif poped in cards2:
            i = cards2.index(poped)
            if i == two_next:
                two_next += 1
            else:
                return "No"
    return "Yes"

a = ["i", "drink", "water"]
b = ["want", "to"]
c = ["i", "want", "to", "drink", "water"]
print(solution(a, b, c))

# https://school.programmers.co.kr/learn/courses/30/lessons/159994
# 각 덱의 인덱스로 순서비교하기.
