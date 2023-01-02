import copy
import heapq
import re
from itertools import combinations, permutations, islice
from collections import defaultdict, OrderedDict, deque, Counter
import math


def solution(new_id):
    # 1
    new_id = new_id.lower()

    # 2
    def pan(munza:str):
        if munza.isalnum():
            return True
        if munza == "-" or munza == "_" or munza == ".":
            return True
        return False

    new_id = list(filter(lambda x: pan(x), list(new_id)))

    # 3
    for i in range(len(new_id)):
        if i == 0:
            continue
        else:
            if (new_id[i-1] == "." or new_id[i-1] == "") and new_id[i] == ".":
                new_id[i] = ""

    """
    # 3-1 : join하고 replace를 쓰는 방법. 전체 길이만큼 이터레이션보단 이게 훨씬 메모리적으론 괜찮아보인다.
    while '..' in answer:
        answer = answer.replace('..', '.')
    """

    # 4
    if new_id[0] == ".":
        new_id[0] = ""
    if new_id[-1] == ".":
        new_id[-1] = ""
    new_id = list("".join(new_id))

    # 5
    if len(list(filter(lambda x: x != "", new_id))) == 0:
        new_id = ["a"]
    # 6
    if len(new_id) >= 16:
        new_id = new_id[0:15]

    if new_id[0] == ".":
        new_id[0] = ""
    if new_id[-1] == ".":
        new_id[-1] = ""

    new_id = list("".join(new_id))

    # 7
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id.append(new_id[-1])

    return "".join(new_id)



a = "...!@BaT#*..y.abcdefghijklm"
b = "z-+.^."
c = "=.="
d = "123_.def"
e = "abcdefghijklmn.p"
for i in [a,b,c,d,e]:
    solution(i)

# https://school.programmers.co.kr/learn/courses/30/lessons/72410
# 뉴비시절 JS로 풀려다가 개털렸던 문제. 지금은 30분정도만에 풀었다. 확실히 예전보다 머리가 잘 돌아가는게 느껴진다.