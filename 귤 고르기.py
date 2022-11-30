import collections


def solution(k, tangerine):
    # Counter와 most_common을 통해서 count횟수가 높은 기준으로 정렬해줍니다.
    # return값이 종류만 원하므로 귤의 크기는 별로 상관 없어보입니다.
    counter = collections.Counter(tangerine).most_common()
    count = 0

    # k가 0이나 음수가 될 때까지 종류 count의 값을 k에서 빼주고, 뺄 때마다 count는 늘려갑니다.
    # count를 0부터 시작하니 인덱스로도 사용할 수 있어서 좋네요.
    while k > 0 :
        k -= counter[count][1]
        count += 1
    # print(count)
    return count


tan = [1, 3, 2, 5, 4, 5, 2, 3]
solution(6, tan)
