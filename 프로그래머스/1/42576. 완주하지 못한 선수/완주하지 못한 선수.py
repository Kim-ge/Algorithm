from collections import Counter

def solution(participant, completion):
    counter1 = Counter(participant)
    counter2 = Counter(completion)
    
    answer = []
    
    for element in counter1:
        if element not in counter2:
            answer.append(element)
        elif counter1[element] > counter2[element]:
            answer.append(element)
    return ', '.join(answer)