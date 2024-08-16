from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    # 가능한 모든 숫자 조합 생성
    possible_numbers = set()
    for i in range(1, len(numbers) + 1):
        # permutations를 통해 각 자리수의 숫자 조합 생성
        perms = permutations(numbers, i)
        for p in perms:
            num = int(''.join(p))
            possible_numbers.add(num)
    
    # 소수 판별
    prime_count = 0
    for num in possible_numbers:
        if is_prime(num):
            prime_count += 1
    
    return prime_count
