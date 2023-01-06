import datetime
from dateutil.relativedelta import relativedelta


def solution(today, terms, privacies):

    ans = []

    today_splitted = today.split(".")
    today_typed = datetime.datetime.strptime(today_splitted[0]+today_splitted[1]+today_splitted[2], "%Y%m%d")

    terms_dict = {}
    for i in terms:
        SI = i.split(" ")
        terms_dict[SI[0]] = int(SI[1])

    for index, i in enumerate(privacies):
        item = i.split(" ")
        kyoo, yak = item[0], item[1]

        kyoo_splitted = kyoo.split(".")
        kyoo_typed = datetime.datetime.strptime(kyoo_splitted[0] + kyoo_splitted[1] + kyoo_splitted[2], "%Y%m%d")
        # print(today_typed, kyoo_typed, yak, today_typed-kyoo_typed)
        delta = relativedelta(months=terms_dict[yak])

        if not kyoo_typed+delta > today_typed:
            ans.append(index+1)
    return ans


a = "2022.05.19"
b = ["A 6", "B 12", "C 3"]
c = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

d = "2020.01.01"
e = ["Z 3", "D 5"]
f = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

solution(a, b, c)
# solution(d, e, f)


# https://school.programmers.co.kr/learn/courses/30/lessons/150370
# 쉬운 구현문제. datetime 모듈과 relativedelta 모듈을 써서 매우 쉽게 날짜 연산이 가능했다.
# 모든 달은 28일까지만 있다는 전제가 붙긴 했지만, 윤년 등의 현실성을 감안해서라도 모듈을 쓰는게 백배 나아보인다. 삶에서 맞닥뜨리는 상황을 해결하기 위해 문제를 푸는거지, 문제를 위해서 문제를 푸는게 아니니까.
