def solution(arr1, arr2):
    ans = [[0 for i in range(len(arr1[0]))] for z in range(len(arr1))]

    def plus_ultra(arr):
        for index, i in enumerate(arr):
            for j in range(len(i)):
                ans[index][j] += i[j]

    plus_ultra(arr1)
    plus_ultra(arr2)

    return ans

a = [[1],[2]]
b = [[3],[4]]
solution(a, b)