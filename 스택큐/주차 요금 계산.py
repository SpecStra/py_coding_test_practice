from collections import deque
from collections import defaultdict
from collections import OrderedDict
import math


def solution(fees, records):
    fee_board = defaultdict(int)
    stack = deque()
    time = deque()
    for i in records :
        source = i.split(" ")
        current_time = int(source[0][:2])*60 + int(source[0][3:])
        if source[2] == "IN" :
            stack.append(source[1])
            time.append(current_time)
        else :
            # del 모듈은 별로 쓰고싶진 않았는데 테케에선 문제없이 잘 되네요.
            st_index = stack.index(source[1])
            del stack[st_index]
            fee_board[source[1]] += current_time - time[st_index]
            del time[st_index]

    for index, i in enumerate(stack) :
        # 마지막 출차는 스택에 순서대로 쌓여있을테니 순서에 대한 if문은 없어도 잘 될겁니다.
        # 1439 = 11:59의 분
        fee_board[i] += 1439 - time[index]

    # 개쩌는 OrderedDict
    fee_board = OrderedDict(sorted(fee_board.items()))
    # print(fee_board)

    ans = []

    # 괜히 헷갈리니까 적어둡시다
    gibon_time = fees[0]
    gibon_fee = fees[1]
    over_time = fees[2]
    over_fee = fees[3]

    for k, v in fee_board.items():
        if v <= fees[0]:
            ans.append(gibon_fee)
        else :
            # int(fees[1] + ((math.ceil(v - fees[0]))/fees[2])*fees[3])
            # 괜히 헷갈리니까 한번 정산하고 갑시다
            jungsan = math.ceil((v - gibon_time) / over_time)
            ans.append(gibon_fee + jungsan*over_fee)

    # print(ans)

    return ans


a = [180, 5000, 10, 600]
b = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
solution(a, b)

# Python의 기본 모듈의 강력함을 알 수 있는 문제. 모듈들의 파워덕분에 생각대로 구현할 수 있었으며 효율성도 챙겼다.