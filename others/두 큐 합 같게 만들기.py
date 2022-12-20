import heapq
from collections import deque


def solution(q1, q2):
    q1 = deque(q1)
    q2 = deque(q2)
    if (sum(q1) + sum(q2)) % 2 != 0:
        return -1

    q1_sum = sum(q1)
    q2_sum = sum(q2)
    q_sum = q1_sum + q2_sum

    max_count = (len(q1) - 1) * 3 + 1
    count = 0

    while q1_sum != q2_sum:
        # print(q1, q2)
        if q1_sum > q2_sum:
            q1_sum -= q1[0]
            q2_sum += q1[0]
            q2.append(q1.popleft())
        elif q1_sum < q2_sum:
            q1_sum += q2[0]
            q2_sum -= q2[0]
            q1.append(q2.popleft())

        if count > max_count:
            return -1
        count += 1
        # print(q1, sum(q1), q2, sum(q2))
        # print("-----------------------")
    print(count)
    return count


a = [3, 2, 7, 2]
b = [4, 6, 5, 1]
solution(a, b)

# list로 하는 경우 시간초과 뜨고, deque로 싹 갈아버리니까 안정적.
# 알고리즘 자체는 바로 알아냈으나, 반복문에서 언제 escape할지 구하는걸 못했었다.
