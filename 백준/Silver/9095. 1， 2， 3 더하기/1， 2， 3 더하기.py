def solve_cases(cases):
    # DP 배열 초기화
    dp = [0] * 12
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    
    # DP 배열 채우기
    for i in range(4, 12):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    # 결과 저장
    results = []
    for n in cases:
        results.append(dp[n])
    
    return results

# 입력 처리
import sys
input = sys.stdin.read
data = input().split()
T = int(data[0])
cases = list(map(int, data[1:]))

# 문제 해결 및 출력
results = solve_cases(cases)
for result in results:
    print(result)
