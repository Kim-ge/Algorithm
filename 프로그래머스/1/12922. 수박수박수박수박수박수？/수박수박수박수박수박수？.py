def solution(n):
    pattern = "수박"
    answer = pattern * (n // 2) + pattern[:n % 2]
    return answer