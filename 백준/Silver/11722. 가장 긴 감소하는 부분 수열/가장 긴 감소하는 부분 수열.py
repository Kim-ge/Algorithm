def longest_decreasing_subsequence(A):
    N = len(A)
    dp = [1] * N
    
    for i in range(1, N):
        for j in range(i):
            if A[i] < A[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# 입력
N = int(input())
A = list(map(int, input().split()))

# 가장 긴 감소하는 부분 수열의 길이 출력
print(longest_decreasing_subsequence(A))
