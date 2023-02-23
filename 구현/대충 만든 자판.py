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


def solution(keymap, targets):

    def find_indices(str_a, search_str):
        output = []
        for i, s in enumerate(str_a):
            if search_str in s:
                output.append(s.index(search_str))
        return output

    result = []
    for i in targets:
        cnt = 0
        for j in list(i):
            r_list = find_indices(keymap, j)
            if r_list:
                cnt += min(r_list)+1
            else :
                result.append(-1)
                break
        if cnt != 0:
            result.append(cnt)

    return result




a = ["ABACD", "BCEFD"]
b = ["ABCD","AABB"]
c = ["AA"]
d = ["B"]
solution(c,d)

# https://school.programmers.co.kr/learn/courses/30/lessons/160586
# 금방 푸는 구현. find_indices함수의 경우 ChatGPT한테 조건을 주고 작성해달라고 했더니 뚝딱 만들어줬다. 역시 도구가 편하다.
