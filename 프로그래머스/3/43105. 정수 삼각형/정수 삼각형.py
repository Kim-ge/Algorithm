def solution(triangle):
    # 삼각형의 높이 구하기
    height = len(triangle)
    
    # DP 테이블 초기화: triangle과 같은 크기
    dp = [[0] * (i + 1) for i in range(height)]
    
    # 가장 아래 행을 DP 테이블에 복사
    dp[-1] = triangle[-1]
    
    # 삼각형의 두 번째 마지막 행부터 위쪽으로 DP 테이블 채우기
    for i in range(height - 2, -1, -1):
        for j in range(len(triangle[i])):
            # 현재 칸의 최대 합을 계산
            dp[i][j] = triangle[i][j] + max(dp[i + 1][j], dp[i + 1][j + 1])
    
    # 삼각형의 꼭대기 칸에 저장된 값이 최대 합
    return dp[0][0]
