import sys
input = sys.stdin.readline

def dfs(row, col, depth, current_sum):
    global max_sum
    # 현재까지의 합 + 남은 최대 가능한 합과 비교하여 가지치기
    if max_sum >= current_sum + max_value * (3 - depth):
        return
    
    # 4개의 셀을 방문했을 때 최대값 갱신
    if depth == 3:
        max_sum = max(max_sum, current_sum)
        return
    
    # 상, 우, 하, 좌로 이동
    for direction in range(4):
        next_row = row + row_directions[direction]
        next_col = col + col_directions[direction]
        
        if 0 <= next_row < N and 0 <= next_col < M and not visited[next_row][next_col]:
            # 현재 셀을 방문한 경우
            if depth == 1:
                visited[next_row][next_col] = True
                dfs(row, col, depth + 1, current_sum + grid[next_row][next_col])
                visited[next_row][next_col] = False
            
            # 현재 셀을 방문한 경우
            visited[next_row][next_col] = True
            dfs(next_row, next_col, depth + 1, current_sum + grid[next_row][next_col])
            visited[next_row][next_col] = False

# 입력 처리
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
row_directions = [-1, 0, 1, 0]
col_directions = [0, 1, 0, -1]
max_sum = 0
max_value = max(map(max, grid))

# 모든 셀에서 DFS 탐색 시작
for row in range(N):
    for col in range(M):
        visited[row][col] = True
        dfs(row, col, 0, grid[row][col])
        visited[row][col] = False

print(max_sum)
