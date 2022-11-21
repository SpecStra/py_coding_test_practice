import numpy as np


def solution(nums):
    left, right = 0, len(nums)-1

    while left < right :

        min(nums[left], nums[right])

        left += 1
        right -= 1


solution([4, 1, 2, 5, 6, 1, 7, 1, 3, 1, 5, 4, 5, 1, 3, 0, 4, 2, 7, 4])
