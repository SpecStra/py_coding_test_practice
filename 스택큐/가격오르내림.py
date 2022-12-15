# 초단위 주식가격 배열중에서 가격이 떨어지지 않은 기간이 몇 초인지 list로 return

def solution(prices):
    obj = []
    pan = [0]*len(prices)

    for index, i in enumerate(prices):
        obj.append({
            "moto_price" : i,
            "index" : index,
        })

        obj = list(filter(lambda x:x["moto_price"] <= i, obj))

        if index != len(prices)-1:
            for j in obj :
                pan[j["index"]] += 1

    return pan


a = [1, 2, 3, 2, 3]
solution(a)

# 논리적 사고 엿먹으라 그래
# 대충 틀리라고 박아놓은 10만, 100만개짜리 테스트 통과 못하면 너 틀린거야~ 이게 K-변별력이다