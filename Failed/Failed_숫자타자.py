import collections


def solution(numbers):
    debug = False
    gajung = []

    def end_debug_print():
        print(f"가중 : {gajung}") if debug is True else None
        print("----------------------------") if debug is True else None

    stage_dict = {
        "1": [0, 0],
        "2": [0, 1],
        "3": [0, 2],
        "4": [1, 0],
        "5": [1, 1],
        "6": [1, 2],
        "7": [2, 0],
        "8": [2, 1],
        "9": [2, 2],
        "0": [3, 1]
    }

    goals = list(numbers)
    current_left = stage_dict["4"]
    current_right = stage_dict["6"]
    for i in goals:
        current_goal = stage_dict[f"{i}"]
        print(f"Right : {current_right}, Left : {current_left}") if debug is True else None
        print(f"Goal : {current_goal}") if debug is True else None
        # 1. 제자리일 경우 가중치 1 주고 continue
        if current_left == current_goal:
            gajung.append(1)
            end_debug_print()
            continue
        elif current_right == current_goal:
            gajung.append(1)
            end_debug_print()
            continue

        # 2. 좌 우 무엇을 움직일지 결정
        goto_right = [
            abs(current_goal[0] - current_right[0]),
            abs(current_goal[1] - current_right[1]),
        ]
        goto_left = [
            abs(current_goal[0] - current_left[0]),
            abs(current_goal[1] - current_left[1]),
        ]
        # 2-1. 왼쪽 오른쪽 같을 경우엔 오른쪽을 움직이도록.
        if sum(goto_left) > sum(goto_right):
            using_hand = ["right", goto_right]
        elif sum(goto_left) < sum(goto_right):
            using_hand = ["left", goto_left]
        else:
            using_hand = ["right", goto_right]
        print(using_hand) if debug is True else None

        # 3. 가중치가 몇인지 파악
        # 이동거리 행렬에서 둘 다 1 이상 (대각선 이동이 더 효율적일 경우)이면 각자 빼고 가중치 3
        # 직각 이동인 경우 해당되는 곳에서만 빼고 가중치 2
        while sum(using_hand[1]) > 0:
            if using_hand[1][0] > 0 and using_hand[1][1] > 0:
                using_hand[1][0] -= 1
                using_hand[1][1] -= 1
                gajung.append(3)
            elif using_hand[1][0] > 0 and using_hand[1][1] == 0:
                using_hand[1][0] -= 1
                gajung.append(2)
            elif using_hand[1][0] == 0 and using_hand[1][1] > 0:
                using_hand[1][1] -= 1
                gajung.append(2)

        # 4. current에 새로 할당
        if using_hand[0] == "left":
            current_left = current_goal
        elif using_hand[0] == "right":
            current_right = current_goal

        end_debug_print()
    print("End : ", sum(gajung))
    return sum(gajung)


a = ["1756", "5138", "7186491448706", "11111011111"]
for ex in a:
    solution(ex)

# 후기 : 정확성 테스트 40점
# 선형적인 최소치는 제대로 구해지나, 내 코드에선 왼쪽 오른쪽 중 어느쪽이든 움직여도 되는 경우에 분기생성이 안되도록 한 쪽으로 고정시켜서 분기에 따른 여러가지의 최소값은 구해내지 못하는 것으로 추정됨.
# 재귀함수로 굴리면 되려나? 뭣같은 테케 넣어놓고 풀라는게 참.. 개발하려고 코테 푸는건지 코테 풀려고 개발하는건지
