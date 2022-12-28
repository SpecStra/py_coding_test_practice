import copy
import heapq
import re
from collections import deque
from itertools import islice
from itertools import combinations, permutations
from collections import defaultdict
from collections import OrderedDict
import math


def solution(str1, str2):
    strs = [str1.upper(), str2.upper()]
    st1 = []
    st2 = []
    for soonseo, src in enumerate(strs):
        for i in range(len(src)-1):
            check_st = src[i:i+2]
            if check_st.isalpha():
                if soonseo == 0 :
                    st1.append(check_st)
                else :
                    st2.append(check_st)
    if len(st1) == 0 and len(st2) == 0:
        return 65536
    # print(st1, st2)
    # hap = [i for i in st1 if i not in st2]+st2

    hap = st1 + st2
    gyo = []

    # 교집합 구하기
    for i in st2 :
        if i in st1 :
            st1.remove(i)
            gyo.append(i)

    # 합집합 구하기. a + b를 한 뒤, 교집합에 이터레이터를 걸어서 a + b에서 루프하여 있다면 그 교집합 원소를 빼준다.
    for i in gyo:
        hap.remove(i)
    # print(hap)
    # print(hap, gyo, int(len(gyo) / len(hap) * 65536))
    return int(len(gyo) / len(hap) * 65536)


a = "BAAAA"
b = "AAA"

c = "E=M*C^2"
d = "e=m*c^2"

e = "aa1+aa2"
f = "AAAA12"
solution(a, b)

# https://school.programmers.co.kr/learn/courses/30/lessons/17677
# 교집합, 합집합 로직이 배울만했던 문제. 나머진 쉽다.
# 주석처리한 합집합으로 시도했을땐 예제 a,b를 넣었을때 안됐다.