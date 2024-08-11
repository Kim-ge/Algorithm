def solution(routes):
    # 차량의 진출 지점 기준으로 정렬
    routes.sort(key=lambda x: x[1])
    
    cameras = 0
    last_camera_position = -30001  # 가능한 최소값
    
    for route in routes:
        start, end = route
        # 현재 카메라가 이 차량의 구간에 포함되지 않는다면
        if last_camera_position < start:
            # 새로운 카메라를 이 차량의 끝 지점에 설치
            cameras += 1
            last_camera_position = end
    
    return cameras
