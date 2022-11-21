# S에 있는 J의 갯수의 합을 반환하세요
import collections


# 해싱
def solution(J, S):
    freqs = {}
    for char in S:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1
    print(freqs)
    # 이하생략


# 카운터
def solution2(J, S):
    count = collections.Counter(list(S))
    ans = 0
    for i in J:
        ans += count.get(i)
        # 이거도 됩니다. ans += count[i]
    print(ans)
    return ans


# 빠요엔
def solution3(J, S):
    # print(sum(s in J for s in S))
    return sum(s in J for s in S)


solution3("aA", "aAAbbbb")
