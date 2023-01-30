from functools import reduce
import sys

sys.setrecursionlimit(10 ** 5)


def solution(maps):
    X = 0
    mini_map = []

    if not maps:
        return [-1]

    for i in maps:
        axo = ",".join(i)
        evaled = eval(f"[{axo}]")
        a = list(map(int, evaled))
        mini_map.append(a)

    ans = []
    cnt = []

    def dfs(i, j):
        if i < 0 or \
                i >= len(mini_map) or \
                j < 0 or \
                j >= len(mini_map[0]) or \
                mini_map[i][j] == 0:
            return

        cnt.append(mini_map[i][j])
        mini_map[i][j] = 0

        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    for i in range(len(mini_map)):
        for j in range(len(mini_map[0])):
            if mini_map[i][j] != 0:
                dfs(i, j)
                ans.append(reduce(lambda x, y: x + y, cnt))
                cnt = []

    # print(sorted(ans))
    return sorted(ans) if ans else [-1]

# https://school.programmers.co.kr/learn/courses/30/lessons/154540
# 왠지 모르게 몇몇 테케에서 런타임 에러 뜨길래 때려쳤던 문제
# 근데 질문글에 어떤 분께서 파이썬 기본 재귀 깊이 초과때문에 그럴 수도 있다면서 재귀 깊이를 늘려주는 코드를 넣어보라고 해서 넣었더니 바로 통과했다.
# DFS도 몇 번 풀다보니까 점점 익숙해지는 것 같다..
