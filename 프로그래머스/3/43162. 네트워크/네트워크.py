def solution(n, computers):
    def dfs(computer):
        #현재 컴퓨터를 방문 처리
        visited[computer] = True
        #연결된 컴퓨터들을 탐색
        for i in range(n):
            if computers[computer][i] == 1 and not visited[i]:
                dfs(i)
    
    visited = [False] * n  #모든 컴퓨터를 방문하지 않은 상태로 초기화
    network_count = 0  #네트워크 개수를 세기 위한 변수
    
    for i in range(n):
        if not visited[i]:  #i번째 컴퓨터가 아직 방문되지 않았다면
            dfs(i)  #해당 컴퓨터로부터 DFS 시작
            network_count += 1  #네트워크 개수 증가
    
    return network_count