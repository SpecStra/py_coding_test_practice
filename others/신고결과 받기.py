import heapq
from collections import deque


def solution(id_list, report, k):
    report = list(set(report))

    get_red = deque([0]*len(id_list))
    give_red = deque([[] for i in range(len(id_list))])

    # 선별
    for i in report :
        listed_report = i.split(" ")
        # print(listed_report)
        attacker = listed_report[0]
        shotted = listed_report[1]
        attacker_index = id_list.index(attacker)
        shotted_index = id_list.index(shotted)
        # print(f"= {give_red[attacker_index]}")
        if shotted not in give_red[attacker_index] :
            give_red[attacker_index].append(shotted)
        get_red[shotted_index] += 1
        # print(get_red, give_red)

    banned = deque()

    # 정지계정
    for index, i in enumerate(get_red):
        if i >= k :
            banned.append(id_list[index])

    # print(banned)

    feedback = deque([0]*len(id_list))

    # 정지 완료 통보
    for index, i in enumerate(give_red):
        for j in banned :
            if j in i :
                feedback[index] += 1

    # print(list(feedback))

    return list(feedback)


a = ["con", "ryan"]
b = ["ryan con", "ryan con", "ryan con", "ryan con"]
solution(a, b, 2)

# 예전에 JS로 하다가 못 풀었던 문제.
# 알고리즘 자체는 구상하는대로 진행했고, deque로 했더니 효율성도 슥슥 넘어간다.
# 알아보기 쉽게 하기 위해서 사람다운 프로세스에 따라 3단계로 구성했으나 머리를 좀 더 굴리면 더 줄일수도 있을듯?