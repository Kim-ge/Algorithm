def solution(numbers, target):
    def dfs(index, current_sum):
        #모든 숫자를 탐색한 경우
        if index == len(numbers):
            #타겟 넘버와 현재 합이 같은 경우
            return 1 if current_sum == target else 0
        
        #현재 숫자를 더하거나 빼는 두 가지 경우에 대해 재귀적으로 탐색
        return dfs(index + 1, current_sum + numbers[index]) + dfs(index + 1, current_sum - numbers[index])
    
    # DFS 탐색 시작
    return dfs(0, 0)