import copy
import heapq
import itertools
import re
from itertools import combinations, permutations, islice
from collections import defaultdict, OrderedDict, deque, Counter
import math
import datetime
from dateutil.relativedelta import relativedelta


def solution(s: str):
    is_x, is_not_x, x, mute = 0, 0, "", ""
    queue = deque(list(s))
    ans = []
    while queue:
        item = queue.popleft()
        if not x and len(queue) > 1:
            x = item
            is_x += 1
            mute += item
            continue
        if x == item:
            is_x += 1
            mute += item
        else :
            is_not_x += 1
            mute += item
        if is_x == is_not_x:
            ans.append(mute)
            is_x, is_not_x, x, mute = 0, 0, "", ""
        if not queue:
            if mute :
                ans.append(mute)

    print(ans)
    return len(ans)



a = ["banana", "abracadabra", "aaabbaccccabba"]
for i in a:
    solution(i)

# https://school.programmers.co.kr/learn/courses/30/lessons/140108
# 저번에 재귀로 풀려다가 틀렸던 문제. 물론 재귀로도 풀 수야 있겠지만 아직 재귀 숙련도가 부족한 모양이다.
# 그래서 큐로 풀었습니다. 10분컷.
