import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    entry_finder = {}  # 현재 힙에 있는 유효한 항목을 추적

    for operation in operations:
        command, num = operation.split()
        num = int(num)
        
        if command == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            if num in entry_finder:
                entry_finder[num] += 1
            else:
                entry_finder[num] = 1
        
        elif command == 'D':
            if num == 1 and max_heap:
                # 최댓값 삭제
                while max_heap and entry_finder.get(-max_heap[0], 0) == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    entry_finder[max_val] -= 1
                    if entry_finder[max_val] == 0:
                        del entry_finder[max_val]
            
            elif num == -1 and min_heap:
                # 최솟값 삭제
                while min_heap and entry_finder.get(min_heap[0], 0) == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    entry_finder[min_val] -= 1
                    if entry_finder[min_val] == 0:
                        del entry_finder[min_val]
    
    # 최종 결과 계산
    while min_heap and entry_finder.get(min_heap[0], 0) == 0:
        heapq.heappop(min_heap)
    while max_heap and entry_finder.get(-max_heap[0], 0) == 0:
        heapq.heappop(max_heap)
    
    if not min_heap or not max_heap:
        return [0, 0]
    
    min_val = min_heap[0]
    max_val = -max_heap[0]
    
    return [max_val, min_val]