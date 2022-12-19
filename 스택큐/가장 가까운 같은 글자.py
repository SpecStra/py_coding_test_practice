import heapq
from collections import deque


def solution(s):
    obj = deque()
    used = []
    ans = []
    for index, i in enumerate(list(s)):
        if i not in used:
            ans.append(-1)
        else:
            for j in obj:
                if j[0] == i:
                    ans.append(index - j[1])
                    break
        used.append(i)
        obj.appendleft([i, index])
    return ans


a = [1, 2, 3, 9, 10, 12]
b = "banana"
solution(b)

# 그냥 [::-1] 인덱싱으로 풀려고 했는데 런타임 에러 뜨길래 deque의 appendleft를 이용한 스택방식으로 선회.