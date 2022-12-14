def solution(n):
    capa = 15
    pack = []
    total: float = 0

    for i in n:
        pack.append((round(i[0] / i[1], 3), i[0], i[1]))

    pack.sort(reverse=True)

    for item in pack:
        if capa > item[2]:
            capa -= item[2]
            total += item[0] * item[2]
        else:
            total += capa * item[0]

    return total


a = [
    (4, 12),
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2)
]
solution(a)
