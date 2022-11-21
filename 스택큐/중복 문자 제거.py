import collections


def solution(nums):
    counter, stack = collections.Counter(nums), []
    print(counter)


solution("cbacdcbc")