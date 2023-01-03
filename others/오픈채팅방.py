import copy
import heapq
import itertools
import re
from itertools import combinations, permutations, islice
from collections import defaultdict, OrderedDict, deque, Counter
import math


def solution(record):
    answer = []

    obj = {}
    for i in record:
        info = i.split(" ")
        if info[0] == "Enter":
            obj[f"{info[1]}"] = info[2]
            answer.append(f"{info[1]}^님이 들어왔습니다.")
        elif info[0] == "Leave":
            answer.append(f"{info[1]}^님이 나갔습니다.")
        elif info[0] == "Change":
            obj[f"{info[1]}"] = info[2]
    # print(obj)
    # print(answer)
    adds = []
    for i in answer:
        spt = i.split("^")
        adds.append(obj[f"{spt[0]}"]+spt[1])
    # print(adds)
    return adds


a = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(a)

# https://school.programmers.co.kr/learn/courses/30/lessons/42888
# 이것도 코린이때 JS로 풀다가 개털렸던 문제. 그때도 object(파이썬에선 dict)를 써서 풀려고 2시간 넘게 아득바득 했는데 지금은 15분만에 풀어버리니 기분이 묘하다.
# dict의 key-value관계를 생각하니 편히 풀 수 있었다. uid로만 로그를 저장한 뒤 다시 순회하면서 uid로 key를 조회해서 대입하는 방식을 썼고, 다른 사람들 풀이를 보니 비슷하게 2번 순회를 많이 쓴 듯 하다.
# 템플릿 리터럴이 참 보기 좋다.