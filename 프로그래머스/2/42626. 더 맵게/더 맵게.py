import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    mix_count = 0
    
    while scoville[0] < K:  
        if len(scoville) < 2:
            return -1 
        

        first = heapq.heappop(scoville) #가장 맵지 않은 음식
        second = heapq.heappop(scoville) #두 번째로 맵지 않은 음식
        new_food = first + (second * 2)
        
        # 섞어 만든 새로운 음식을 힙에 넣고 섞은 횟수 증가
        heapq.heappush(scoville, new_food)
        mix_count += 1
    
    return mix_count
