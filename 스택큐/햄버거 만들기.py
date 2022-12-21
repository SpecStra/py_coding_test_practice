import heapq
from collections import deque
from itertools import islice
from collections import defaultdict
from collections import OrderedDict
import math


def solution(ingredient):
    stack = deque()
    ans = 0
    for index, i in enumerate(ingredient):
        stack.append(i)
        print(stack)
        if len(stack) > 3 and stack[-1] == 1 and stack[-2] == 3 and stack[-3] == 2 and stack[-4] == 1:
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            ans += 1

    return ans


a = [1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
b = []
solution(a)

# https://school.programmers.co.kr/learn/courses/30/lessons/133502
# 어렵게 생각하면 틀린다.