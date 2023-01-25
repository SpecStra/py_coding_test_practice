import copy
import heapq
import itertools
import re
from itertools import combinations, permutations, islice
from collections import defaultdict, OrderedDict, deque, Counter
import math
import datetime
from dateutil.relativedelta import relativedelta
from functools import reduce


def solution(m):

    ans = []

    for i in m:
        del_arr = list(filter(lambda x: x != i, m))
        ans.append(reduce(lambda x, y: x*y, del_arr))

        # join과 eval을 활용하는 신박한 방법도 있다.
        # eval('*'.join([str(n) for n in del_arr]))

    print(ans)

    return ans


solution([3, 2, 1])