def find_year(E, S, M):
    year = 1
    e, s, m = 1, 1, 1
    while True:
        if e == E and s == S and m == M:
            return year
        e += 1
        s += 1
        m += 1
        if e > 15:
            e = 1
        if s > 28:
            s = 1
        if m > 19:
            m = 1
        year += 1

# 입력을 받습니다.
E, S, M = map(int, input().split())

# 결과를 출력합니다.
print(find_year(E, S, M))
