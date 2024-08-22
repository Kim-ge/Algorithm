from collections import deque

def solution(maps):
    # 맵의 크기
    n = len(maps)
    m = len(maps[0])
    
    # 방향 배열 (동, 서, 남, 북)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # BFS를 위한 큐 초기화
    queue = deque([(0, 0)])  # (행, 열)
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    # 거리 배열 초기화
    distance = [[-1] * m for _ in range(n)]
    distance[0][0] = 1  # 시작점의 거리는 1
    
    while queue:
        x, y = queue.popleft()
        
        # 도착 지점에 도달했으면 거리 반환
        if x == n - 1 and y == m - 1:
            return distance[x][y]
        
        # 상하좌우 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 이동 가능 범위 체크
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
    
    # 도착할 수 없는 경우
    return -1