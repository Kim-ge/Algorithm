def find_k(M, N, x, y):
    # x와 y가 각각 M과 N을 초과하는 경우 -1 반환
    if x > M or y > N:
        return -1

    # x가 x % M, y가 y % N이 되는 해를 찾기 위한 초기 값 설정
    k = x
    while k <= M * N:
        if (k - 1) % N + 1 == y:
            return k
        k += M
    return -1

# 입력 처리
import sys
input = sys.stdin.read
data = input().split()
T = int(data[0])

results = []
index = 1
for _ in range(T):
    M = int(data[index])
    N = int(data[index + 1])
    x = int(data[index + 2])
    y = int(data[index + 3])
    result = find_k(M, N, x, y)
    results.append(result)
    index += 4

# 결과 출력
for result in results:
    print(result)
