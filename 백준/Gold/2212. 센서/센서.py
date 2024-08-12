def min_total_length(N, K, sensor_positions):
    #센서 위치 정렬
    sensor_positions.sort()
    
    #센서 사이의 거리 차이 계산
    distances = []
    for i in range(1, N):
        distances.append(sensor_positions[i] - sensor_positions[i - 1])
    
    #거리 배열을 내림차순으로 정렬
    distances.sort(reverse=True)
    
    #K개의 구간을 만들기 위해 가장 큰 K-1개의 거리 제외
    #전체 거리의 합에서 가장 큰 K-1 개의 거리 빼기
    min_total_length = sum(distances[K-1:]) if K <= N else 0
    
    return min_total_length


import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
K = int(data[1])
sensor_positions = list(map(int, data[2:]))

print(min_total_length(N, K, sensor_positions))
