# 일정 금액 지불 시 10일동안 회원자격
# 회원 대상으로 매일 한 가지 제품 할인
# -> 제품과 수량이 할인하는 날짜와 10일 연속으로 일치하는 경우에 맞춰서 회원자격을 얻으려 한다.

# want : 원하는 제품
# number : 원하는 제품의 각 수량
# discount : 실제 할인하는 제품들
# return : 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수의 갯수 (3일이면 3)

def solution(want, number, discount):
    ans = 0
    for j in range(len(discount)-9):
        for_dis = discount[j:j+10]
        for_want = [*want]
        for_num = [*number]
        for i in for_dis:
            try :
                found = for_want.index(i)
                for_num[found] -= 1
            except ValueError :
                # needs error handle
                continue
            print(for_num)
        # print(for_dis, f"{j}:{j+10}", len(for_dis))
        if for_num.count(0) == len(for_num) :
            ans += 1
            print("ans added")
        print("--------------------------")

    print(f"ans : {ans}")
    return ans