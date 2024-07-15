def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

N = int(input())
numbers = list(map(int, input().split()))

count_primes = 0
for number in numbers:
    if is_prime(number):
        count_primes += 1

print(count_primes)
