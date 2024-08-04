def solution(clothes):
    from collections import defaultdict

    # 종류별로 의상을 저장
    clothes_dict = defaultdict(list)
    
    # 의상을 종류별로 분류
    for name, kind in clothes:
        clothes_dict[kind].append(name)
    
    # 각 종류별로 입을 수 있는 경우의 수를 계산
    combinations = 1
    for kind in clothes_dict:
        combinations *= (len(clothes_dict[kind]) + 1)  # 해당 종류의 의상 수 + 아무 것도 안 입는 경우
    
    # 아무 것도 입지 않는 경우 1가지를 제외
    return combinations - 1
