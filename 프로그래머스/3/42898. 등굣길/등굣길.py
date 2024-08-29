def solution(m, n, puddles):
    # dp 테이블 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1  # 시작점

    # 물에 잠긴 지역 표시
    for x, y in puddles:
        dp[y][x] = -1
    
    # dp 채우기
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1:  # 물에 잠긴 지역
                dp[i][j] = 0
            else:
                if i > 1:
                    dp[i][j] += dp[i-1][j]
                if j > 1:
                    dp[i][j] += dp[i][j-1]
                dp[i][j] %= 1000000007
    
    return dp[n][m]
