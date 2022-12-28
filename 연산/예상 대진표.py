import copy
import heapq
import re
from collections import deque
from itertools import islice
from itertools import combinations, permutations
from collections import defaultdict
from collections import OrderedDict
import math


def solution(n,a,b):
    if a%2 == 0:
        a -= 1
    if b%2 == 0 :
        b -= 1
    print("This = ",a, b)
    if a == b :
        return 1

    ranged = deque(range(1, n+1))
    count = 1
    for i in range(int(math.log2(n))):
        a_index = ranged.index(a)
        b_index = ranged.index(b)
        print(a_index, b_index)
        # print(min([a_index, b_index]) % 2, bool(min([a_index, b_index]) % 2), max([a_index, b_index]) % 2 == 0)

        if abs(a_index - b_index) == 1 :
            if a_index == 0 and b_index == 1:
                print(f"end : {ranged}", count)
                return count
            if min([a_index, b_index]) % 2 != 1 and max([a_index, b_index]) % 2 != 0:
                print(f"end : {ranged}", count)
                return count

        if a_index%2 != 0 :
            ranged[a_index] = ranged[a_index-1]
            ranged[a_index - 1] = a
        if b_index%2 != 0 :
            ranged[b_index] = ranged[b_index-1]
            ranged[b_index - 1] = b

        ranged = list(filter(lambda x : ranged.index(x) % 2 == 0, ranged))
        print(ranged, f"round {count}")
        count += 1
    return count


def solution2(n,a,b):
    answer = 0
    while True:
        answer += 1
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        if a == b or a == 0 or b == 0:
            break
    return answer


a = "BAAAA"
b = "AAA"
c = "E=M*C^2"
d = "e=m*c^2"
e = "aa1+aa2"
f = "AAAA12"
solution(8, 4, 7)

# https://school.programmers.co.kr/learn/courses/30/lessons/12985

# sol1이 내가 푼 것.
# 1. 홀수 인덱스가 무조건 이기게 설계하고,
# 2. 반씩 줄여나가는 와중에 a나 b의 인덱스가 짝수가 될 경우 홀수랑 바꿔주고
# 3. 체크하기
# 정확성은 다 맞는데 효율성에서 전부 빠꾸먹음. 인덱스 바꾸는 부분에서 문제가 생기겠거니 하긴 했는데, 2**20까지 주는 문제가 너무 무자비하다.

# sol2가 지나가다 본 답. 걍 창의력 문제라고 해도 믿겠네..
