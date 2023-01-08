import copy
import heapq
import itertools
import re
from itertools import combinations, permutations, islice
from collections import defaultdict, OrderedDict, deque, Counter
import math
import datetime
from dateutil.relativedelta import relativedelta


def solution(numbers):
    listed_nums = list(numbers)

    ans = []

    def is_prime_number(x):
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    for i in range(len(numbers)):
        # print(list(permutations(listed_nums, i+1)))
        for j in list(permutations(listed_nums, i+1)):
            if is_prime_number(int("".join(j))) and int("".join(j)) not in ans and int("".join(j)) != 1 and int("".join(j)) != 0:
                ans.append(int("".join(j)))
    # print(ans)
    return len(ans)


a = "17"
b = "011"
c = "17084"
solution(b)

# https://school.programmers.co.kr/learn/courses/30/lessons/42839
# permutations을 활용하여 가볍게 풀 수 있었던 완전탐색 문제. 소수 판별식은 자주 쓰는 모듈에서 가져왔다.
