import sys
import math

input = sys.stdin.read
M, N = map(int, input().split())

# 에라토스테네스의 체를 사용한 소수 판별
is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False # 0과 1은 소수가 아님

for i in range(2, int(math.sqrt(N)) + 1):
    if is_prime[i]:
        for j in range(i * i, N + 1, i):
            is_prime[j] = False

# M 이상 N 이하의 소수 출력
for num in range(M, N + 1):
    if is_prime[num]:
        print(num)
