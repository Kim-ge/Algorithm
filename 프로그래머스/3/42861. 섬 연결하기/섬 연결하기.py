def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        parent[rootY] = rootX

def solution(n, costs):
    # 간선을 비용을 기준으로 정렬
    costs.sort(key=lambda x: x[2])
    
    parent = [i for i in range(n)]
    total_cost = 0
    
    for u, v, cost in costs:
        # 두 노드의 루트가 다르면 (즉, 연결되지 않았으면)
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            total_cost += cost
    
    return total_cost
