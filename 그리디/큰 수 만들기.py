import copy
import heapq
import itertools
import re
from itertools import combinations, permutations, islice
from collections import defaultdict, OrderedDict, deque, Counter
import math


def solution(number, k):
    stack = []
    for num in number:
        # stack 원소가 존재, 스택의 우측 끄트머리보다 현재 num이 더 클 경우, k가  1 이상
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return "".join(stack)


a = ["119", "97674223", "1195524421"]
solution(a)

# https://school.programmers.co.kr/learn/courses/30/lessons/42883
# 그리디 알고리즘, 큰 수 만들기
# 순환하면서 현재 num보다 작은 stack 내부의 것들을 pop 해버리는 것.
# 큰 자릿수의 숫자가 우선시된다는걸 간과해서 제대로 풀지 못했었다.