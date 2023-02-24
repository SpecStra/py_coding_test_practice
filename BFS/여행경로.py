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


# 주어진 항공권은 모두 사용해야 합니다.
# 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
# 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

def solution(tickets):
    obj = defaultdict(list)
    for i in tickets:
        if not obj[i[0]]:
            obj[i[0]] = [i[1]]
        else:
            obj[i[0]].append(i[1])
    sorted_dict = {k: sorted(v) for k, v in obj.items()}

    # print(sorted_dict)

    def go_test(que_status, start, dec):
        que = deque()
        que.append(dec)
        if start:
            que_status[start].pop(que_status[start].index(dec))
        process = []
        # print(f"{que_status} 상태에서 {dec}부터 시작합니다")
        while que:
            # print(que_status)
            try:
                if que_status[que[0]]:
                    if len(que_status[que[0]]) > 1:
                        que_hubo = []
                        for ine in que_status[que[0]]:
                            que_hubo.append(len(go_test(copy.deepcopy(que_status), que[0], ine)))
                        max_que_hubo = que_hubo.index(max(que_hubo))
                        que.append(que_status[que[0]].pop(max_que_hubo))
                    else:
                        que.append(que_status[que[0]].pop(0))
                process.append(que.popleft())
            except KeyError:
                process.append(que.popleft())
                break
        # print(f"complete progress : {process}")
        return process

    return go_test(que_status=sorted_dict, start=None, dec="ICN")


b = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
a = [["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]
c = [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]
d = [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]
e = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"],
     ["COO", "BOO"]]

solution(e)

# https://school.programmers.co.kr/questions/41718
# obj로 바꿔서 큐 처리. 중간에 분기 생길때 전부 순회하는 쪽으로 골라야 한다길래 재귀 하나 넣음.
# 사람들이 고려해봐야 된다는 테케는 다 통과. 정확도는 문제 없어 보이는데 시간에서 걸리는듯.
# 전부 고려해야만 되게 해두고 시간 넘길만큼 긴 테케 넣어두는건 양심이 좀 없지 않나? 경시대회 하는것도 아닌데 뭐 이딴걸 넣어두는건지 모르겠네. 문제도 그냥 leetcode에 있는거 문자만 바꿔서 베껴온거더만.
