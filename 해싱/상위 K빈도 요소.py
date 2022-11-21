import collections


# 상위 K번 이상 등장하는 요소의 list를 리턴하세요
# 내 풀이 (탐?색이 되네) <- 가급적 most_common을 이용하는 형태로 바꾸는 편이 좋을듯.
def solution(nums, K):
    count = collections.Counter(nums)
    ans = [i for i in count if i <= K]
    print(ans)
    
    # 1줄로
    return [i for i in collections.Counter(nums) if i <= K]


# 빠요엔
def solution2(nums, K):
    # 튜플로 (key : value)형태로 나옵니다.
    ans = list(zip(*collections.Counter(nums).most_common(K)))[0]
    print(ans)
    return ans


solution2([1,1,1,2,2,3], 2)
