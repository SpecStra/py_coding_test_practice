import copy
import heapq
import itertools
import re
from itertools import combinations, permutations, islice
from collections import defaultdict, OrderedDict, deque, Counter
import math


def solution(numbers, target):
    ans = 0
    after = []
    for z in range(0, 2):
        for i in range(0, len(numbers)):
            stack = []
            nao = copy.deepcopy(numbers)

            def sol(nums:list):
                for j in nums:
                    if sum(stack) <= target:
                        stack.append(j)
                    elif sum(stack) > target:
                        stack.append(-j)
                    # print(stack)
                if sum(stack) == target:
                    if stack not in after:
                        after.append(stack)

            if z == 0:
                sol(nao)
            else :
                nao[i] = -nao[i]
                sol(nao)

    print(after)
    return len(after)


def solution2(numbers, target):
    if not numbers:
        if target == 0:
            return 1
        else:
            return 0
    else:
        return solution2(numbers[1:], target+numbers[0]) + solution2(numbers[1:], target-numbers[0])


a = [1, 1, 1, 1, 1]
b = [4, 1, 2, 1]
solution(a, 3)


# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 내 솔루션을 틀렸고, sol2가 정답 가져온 것.
# 원리는 이해 되는데.. for로 했을땐 재귀처럼 많은 경우의 수를 다 포함 못해서 내 솔루션이 틀리나보다.
