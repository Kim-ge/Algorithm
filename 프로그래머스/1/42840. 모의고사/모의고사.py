def solution(answers):
    #각 수포자의 답안 패턴 정의
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    #각 수포자가 맞힌 문제 수를 저장할 리스트
    scores = [0, 0, 0]
    
    #정답과 각 패턴을 비교하여 맞힌 문제 수 계산
    for i, answer in enumerate(answers):
        if answer == pattern1[i % len(pattern1)]:
            scores[0] += 1
        if answer == pattern2[i % len(pattern2)]:
            scores[1] += 1
        if answer == pattern3[i % len(pattern3)]:
            scores[2] += 1
    
    #가장 높은 점수 계산
    max_score = max(scores)
    
    #가장 높은 점수를 받은 수포자(들)을 찾기
    result = []
    for i in range(3):
        if scores[i] == max_score:
            result.append(i + 1)
    
    return result