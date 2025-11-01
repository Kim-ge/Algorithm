from collections import Counter

def solution(participant, completion):
    answer = ''
    p_count=Counter(participant)
    c_count=Counter(completion)
    
    answer = p_count - c_count

    return list(answer.keys())[0]