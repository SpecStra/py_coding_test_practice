from collections import deque


def solution(bridge_length, weight, truck_weights):
    queue = deque([0] * bridge_length)
    orders = deque(truck_weights)
    time = 0
    total = 0
    while orders:
        print(queue, orders, total)
        time += 1
        total -= queue[0]
        queue.popleft()
        if total + orders[0] > weight:
            print("case1")
            queue.append(0)
        else:
            w = orders.popleft()
            print("case2")
            total += w
            queue.append(w)
        print(queue, orders, total)
        print("---------------------------")
    print(time + bridge_length)
    return time + bridge_length


solution(2, 10, [1,2,3,4,7])

"""
큐 크기를 brideg_length로 제한하고, 중량 초과일 경우 0을 넣어준다는 발상을 못했었습니다..
total : 현재 하중.
if 현재 하중 + 추가 적재 시 다리 하중 : 현재 다리에 있는 애들만 1칸 진행
else : 현재 다리의 끝에 있는 얘 빼고 추가 적재 및 현재 하중 재계산.
"""
