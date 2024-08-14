def solution(sizes):
    max_width = 0
    max_height = 0
    
    for width, height in sizes:
        # 각 명함의 가로와 세로 길이 중에서 더 큰 값을 가로 방향으로 설정
        # 작은 값을 세로 방향으로 설정
        if width > height:
            max_width = max(max_width, width)
            max_height = max(max_height, height)
        else:
            max_width = max(max_width, height)
            max_height = max(max_height, width)
    
    # 지갑의 크기 계산(가로 * 세로)
    return max_width * max_height