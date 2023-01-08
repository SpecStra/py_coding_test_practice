import copy
import heapq
import itertools
import re
from itertools import combinations, permutations, islice
from collections import defaultdict, OrderedDict, deque, Counter
import math
import datetime
from dateutil.relativedelta import relativedelta


def solution(brown, yellow):

    # 1
    def give_all_divisor(x: int):
        ad = []
        index = 1
        while index <= x:
            if x % index == 0:
                ad.append(index)
            index += 1
        return ad

    # 1-1
    if yellow == 1:
        return [3,3]

    # 2
    yellow_divisor = give_all_divisor(yellow)
    # print(yellow_divisor, list(combinations(yellow_divisor, 2)))
    possible = list(filter(lambda x: x[1]*x[0] == yellow, list(combinations(yellow_divisor, 2))))

    # test 2 : var zegob appended
    zegob = list(filter(lambda x: x*x == yellow, yellow_divisor))
    if zegob:
        possible.append((zegob[0], zegob[0]))

    # print(possible)
    # 3
    for i in possible:
        if (i[0]*2)+(i[1]*2)+4 == brown:
            # print(i)
            return sorted(list(map(lambda x: x+2, i)), reverse=True)

solution(16, 16)

# https://school.programmers.co.kr/learn/courses/30/lessons/42842

# 발상 및 1. : yellow의 모양이 결국 모든걸 결정한다고 생각하고, yellow가 취할 수 있는 모양의 갯수를 구하기로 생각했다.
# 1-1 : 1로 약수를 구할 경우 None이 반환되고, yellow에 1이 나오면 brown은 무조건 8이 되기에, 예외문을 하나 넣어주었다.
# 2 : yellow의 약수들 중 둘이 곱해서 yellow가 되는 쌍을 구했다.
# test2 추가 : 13가지 테스트케이스 중 3개가 틀리길래 트러블슈팅을 해본 결과, 이렇게 하면 자신*자신 = yellow가 되는 경우를 못잡았다.
# 그래서 선별 이후 filter를 한 번 거쳐서 자신이랑 곱해서 yellow가 되는 수가 있다면 튜플로 넣어줫다.
# 3 : 이렇게 나온 yellow의 모양 경우의 수를 모두 거쳐서 brown과 일치하는지 판별한다.

# 다른 풀이를 보니 길이-넓이 공식으로 근의 공식을 통해 구해내더라. 접근방식은 같은데 수학자들의 방식이 더 보기 편해보이긴 한다.
