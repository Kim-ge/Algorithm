from collections import defaultdict

def solution(tickets):
    # 그래프 초기화
    graph = defaultdict(list)
    
    # 그래프 구성: 시작 공항을 키로 하고, 도착 공항들을 리스트로 저장
    for start, end in sorted(tickets, reverse=True):
        graph[start].append(end)
    
    route = []  # 경로를 저장할 리스트
    
    def dfs(airport):
        while graph[airport]:
            next_airport = graph[airport].pop()
            dfs(next_airport)
        route.append(airport)
    
    dfs("ICN")  # 항상 "ICN"에서 출발
    
    return route[::-1]  # 역순으로 경로 반환

