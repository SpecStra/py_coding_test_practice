import copy
import heapq
import re
from itertools import combinations, permutations, islice
from collections import defaultdict, OrderedDict, deque, Counter
import math

# https://school.programmers.co.kr/learn/courses/30/lessons/12981
# 1. 끝말잇기니까 뒤-앞 단어가 같아야 함
# 2. 한 번 말했던 단어는 또 사용할 수 없음
# 3. 한 글자인 단어를 말할 경우 탈락
# return : 탈락한 사람의 번호(1~n)와 몇 번째 차례에서 탈락했는지(1~m)


def solution(n, words):
    past_words = []
    for index, i in enumerate(words):
        if index == 0:
            past_words.append(i)
            continue
        print(words[index - 1][-1:], words[index][0:1])

        def ans(ind):
            sunseo = ind + 1
            cnt = 0
            while sunseo > 0:
                sunseo -= n
                cnt += 1
            sunseo += n
            # print([sunseo, cnt])
            return [sunseo, cnt]
        if len(i) < 2:
            return ans(index)
        if words[index - 1][-1:] != words[index][0:1]:
            return ans(index)
        if i in past_words:
            return ans(index)
        else:
            past_words.append(i)
    return [0, 0]


a = ["land", "dream", "mom", "mom", "ror"]
b = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather",
     "refer", "reference", "estimate", "executive"]
c = ["hello", "one", "even", "never", "now", "world", "draw"]
d = ['ac','ca','ac','ac']
solution(2, ['ac','ca','ac','ac'])

# 보자마자 딱 어떻게 풀어야겠다고 생각은 들었고 그대로 풀었는데..
# 순서랑 몇 번째 사람인지 구하는 ans 함수 짜는데 오래걸렸다. 풀고나면 암것도 아닌데 참 왜이렇게 헤메는지..