def num_ways_to_tile(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007
    
    return dp[n]

# 입력
n = int(input())

# 결과 출력
print(num_ways_to_tile(n))
