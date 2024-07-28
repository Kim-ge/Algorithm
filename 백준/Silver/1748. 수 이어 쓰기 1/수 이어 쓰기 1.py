def calculate_total_digits(N):
    total_digits = 0
    length = 1
    count = 9
    
    while N > 0:
        if N >= count:
            total_digits += count * length
            N -= count
            length += 1
            count *= 10
        else:
            total_digits += N * length
            N = 0
    
    return total_digits

# 입력 처리
import sys
input = sys.stdin.read
N = int(input().strip())

# 결과 출력
print(calculate_total_digits(N))
