import sys

def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    T = [0] * N
    P = [0] * N
    dp = [0] * (N + 2)

    for i in range(N):
        t, p = map(int, input().split())
        T[i] = t
        P[i] = p

    for i in range(N - 1, -1, -1):
        time = i + T[i]
        if time <= N:
            dp[i] = max(P[i] + dp[time], dp[i + 1])
        else:
            dp[i] = dp[i + 1]

    print(dp[0])

if __name__ == "__main__":
    main()
