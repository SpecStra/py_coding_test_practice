import random
import matplotlib.pyplot as plt
import numpy as np

# 상품의 구매단가/판매단가/주문단가/재고비용
pc_price = {
    "buy": 60,
    "sell": 80,
    "order": 50,
    "cost": 1
}

# 해당 재고량 이하로 내려가면 주문, 주문 시 주문하는 양
order_source = [10, 30]
# 난수 지표
rand_source = [3, 4, 4, 5, 5, 5, 6, 6, 6, 7]

# 오늘의 수요량 선언
rand_demand = 0

# 현재 재고량
current_supply = 40

# 오늘의 지표
daily = {
    "profit": 0,
    "cost": 0,
    "net": 0,
}
# 총 지표
all_cycle = {
    "profit": 0,
    "cost": 0,
    "net": 0,
}

# 주문 시 state가 True가 되며, count가 2(3일)이 되면 주문이 완료되고 초기화
order_gaze = {
    "state": False,
    "count": 0,
}
# 데이터
profit_arr = []
net_arr = []
service_arr = []
ten_counter = 0

service_per = 0

# 시뮬레이션 횟수
sim_range = 500

for i in range(0, sim_range):
    daily_profit = 0
    daily_cost = 0
    today_demand = 0
    daily_net = 0

    if order_gaze["state"] is True:
        if order_gaze["count"] == 2:
            print("❗Order has received")
            order_gaze["state"] = False
            current_supply += order_source[1]
            order_gaze["count"] = 0
        else:
            print("❗Waiting Order...")
            order_gaze["count"] += 1

    today_demand = rand_source[random.randrange(0, 9)]
    real_demand = today_demand
    print(f"Today's Demand : {today_demand}, Current pc : {current_supply}")
    if today_demand >= current_supply:
        print("need more supply...")
        today_demand = current_supply
    service_per += today_demand/real_demand

    current_supply = current_supply - today_demand

    if current_supply <= order_source[0] and order_gaze["state"] is False:
        order_gaze["state"] = True
        daily_cost = pc_price["order"]
        print("❗Order has requested")

    daily_profit = today_demand * (pc_price["sell"] - pc_price["buy"])
    daily_cost += current_supply * pc_price["cost"]
    daily_net = daily_profit - daily_cost

    daily["profit"] = daily_profit
    daily["cost"] = daily_cost
    daily["net"] = daily_net

    print(f"Day {i+1}")

    print(daily, "\n")

    all_cycle["profit"] += daily_profit
    all_cycle["cost"] += daily_cost
    all_cycle["net"] += daily_net

    ten_counter += 1
    if ten_counter == 10 :
        profit_arr.append(all_cycle["profit"])
        net_arr.append(all_cycle["cost"])
        service_arr.append(service_per)
        ten_counter = 0


print("------------------------------")

print(all_cycle)
print("총이익 :", all_cycle["net"])
print("서비스 비율", round(service_per/sim_range * 100, 2), "%")

print(profit_arr)
print(net_arr)
print(service_arr)