# 높이의 배열인 arr을 받아서 얼마나 많은 물이 쌓일 수 있는지 계산
from collections import deque
import itertools


def solution(height):
    stack = []
    volume = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            if not len(stack):
                break

            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters
        stack.append(i)
    print(volume)
    return volume


def solution2(height):
    if not height:
        return 0

    volume = 0
    # left, right = 0, 인덱스의 끝번
    left, right = 0, len(height) - 1
    # left_max, right_max = 첫value, 막value
    left_max, right_max = height[left], height[right]
    while left < right:
        print(f"situ : {left, right} || {left_max, right_max} || volume : {volume}")
        # 현재값이냐 원래 max값이냐, 더 큰 값이 max가 된다.
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)

        # 더 높은 쪽으로 투 포인터 이동
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    print(volume)
    return volume


a = [4, 2, 3]
b = [0, 1, 0, 2, 1, 0, 1, 3, 4, 3, 2, 0]
solution2(b)
