def solution(name):
    n = len(name)
    answer = 0
    
    #알파벳 변경 최소 횟수 계산
    for char in name:
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
    
    #커서 이동 최소 횟수 계산
    min_move = n - 1  # 기본적으로 오른쪽으로 쭉 가는 경우
    for i in range(n):
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        # i까지 갔다가 다시 돌아가서 next_i부터 끝까지 가는 경우
        min_move = min(min_move, i + i + n - next_i)
        # 반대 방향으로 가는 경우
        min_move = min(min_move, (n - next_i) * 2 + i)
    
    answer += min_move
    return answer