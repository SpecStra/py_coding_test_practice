def solution(land):
    # 같은 메모리를 가리키는 복제를 만듭니다.
    dp = land
    for i in range(1, len(land)):
        for j in range(4):
            # i-1단계에서 선택했을떄 최적값을 i에 넣어주면서 더해나갑니다. 최종적으로 마지막 리스트의 최대값이 답이 됩니다.
            dp[i][j] += max(dp[i-1][:j] + dp[i-1][j+1:])
            print(dp[i-1][:j] + dp[i-1][j+1:], dp)
    return max(dp[len(dp)-1])


a = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
b = [[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]
solution(a)