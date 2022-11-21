import collections


def solution(subst):
    used = {}
    # 깔삼한 슬라이드 윈도우-포인팅 기법
    max_length = start = 0
    for index, char in enumerate(subst):
        # 이미 나왔던 문자라면 start 위치 갱신
        if char in used:
            start = used[char] + 1
        else :
            max_length = max(max_length, index - start + 1)

        used[char] = index


solution("abcabcbb")
