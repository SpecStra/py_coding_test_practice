import copy
import heapq
import itertools
import re
from itertools import combinations, permutations, islice
from collections import defaultdict, OrderedDict, deque, Counter
import math


def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    cities = list(map(lambda x: x.upper(), cities))
    answer = 0
    cache = deque([])
    city_copy = cities.copy()
    for ref in city_copy:
        if ref not in cache:
            if len(cache) < cacheSize:
                cache.append(ref)
            else:
                cache.popleft()
                cache.append(ref)
            answer += 5
        else:
            cache.remove(ref)
            cache.append(ref)
            answer += 1
    return answer


a = ''
solution(a)

# https://school.programmers.co.kr/learn/courses/30/lessons/17680
# LRU 알고리즘을 구현하는 문제. 캐시가 뭔소린지 검색해봤는데 별거 아니었다.
# 1. 캐시 사이즈보다 작으면 그냥 in
# 2. 캐시 사이즈보다 큰 경우, 가장 묵은걸 out하고 새로 in -> 캐시hit이므로 +5
# 3. 캐시 miss인 경우 해당 city를 지운 뒤 다시 삽입. -> miss이므로 +1
