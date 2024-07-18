n = int(input())
board = [list(input().strip()) for _ in range(n)]

def get_max_length(board, n):
    max_len = 1
    for i in range(n):
        row_len = 1
        col_len = 1
        for j in range(1, n):
            if board[i][j] == board[i][j - 1]:
                row_len += 1
            else:
                row_len = 1
            if board[j][i] == board[j - 1][i]:
                col_len += 1
            else:
                col_len = 1
            max_len = max(max_len, row_len, col_len)
    return max_len

max_candies = 0

for i in range(n):
    for j in range(n):
        if j + 1 < n:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            max_candies = max(max_candies, get_max_length(board, n))
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
        if i + 1 < n:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            max_candies = max(max_candies, get_max_length(board, n))
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(max_candies)
