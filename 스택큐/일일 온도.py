# 지금보다 더 따뜻한 날씨를 위해선 며칠 기다려야 되는지에 대한 []을 리턴하세요
import collections


# 내 풀이
def solution(arr):
    ans = []
    for n in range(len(arr)):
        current = arr[n]
        # print(current, arr[n+1:])
        if len(arr[n + 1:]) == 0:
            # print(0)
            ans.append(0)
            continue
        for i, j in enumerate(arr[n + 1:]):
            if j > arr[n]:
                # print(i+1)
                ans.append(i + 1)
                break
            else:
                if len(arr[n + 1:]) <= 1:
                    # print(0)
                    ans.append(0)
                    break
    print(ans)
    return ans


def solution2(arr):
    ans = [0] * len(arr)
    stack = []
    for i, cur in enumerate(arr):
        while stack and cur > arr[stack[-1]]:
            last = stack.pop()
            ans[last] = i - last
        stack.append(i)
    return ans


solution2([73, 74, 75, 71, 69, 72, 76, 73])
