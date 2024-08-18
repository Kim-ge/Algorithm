def solution(word):
    letters = ['A', 'E', 'I', 'O', 'U']
    position_weight = [781, 156, 31, 6, 1]  # 각 자리별 가중치
    result = 0

    for i, char in enumerate(word):
        index = letters.index(char)
        result += index * position_weight[i] + 1

    return result