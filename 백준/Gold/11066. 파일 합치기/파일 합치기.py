def min_cost_to_merge_files(chapters):
    n = len(chapters)
    dp = [[0] * n for _ in range(n)]
    sum_values = [0] * (n + 1)
    
    # 구간 합 계산
    for i in range(1, n + 1):
        sum_values[i] = sum_values[i-1] + chapters[i-1]
    
    # DP 테이블 채우기
    for length in range(2, n + 1):  # 부분 문제의 길이
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + sum_values[j+1] - sum_values[i]
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n-1]

# 입력 처리
t = int(input())
for _ in range(t):
    k = int(input())
    chapters = list(map(int, input().split()))
    print(min_cost_to_merge_files(chapters))
