def solution(word):
    letters = ['A', 'E', 'I', 'O', 'U']
    result = 0
    
    # 각 자리수별 가중치를 계산
    position_weight = []
    for i in range(5):
        weight = sum(5 ** j for j in range(5 - i))
        position_weight.append(weight)
    
    # 입력된 word에 대해 순서 계산
    for i, char in enumerate(word):
        index = letters.index(char)
        result += index * position_weight[i] + 1

    return result