def solution(routes):
    # 출발 지점 기준으로 오름차순 정렬
    routes.sort()

    # 첫 번째 차량의 도착지점으로 초기 카메라 기준점 설정
    now_camera_position = routes[0][1]
    camera_count = 1

    # 두 번째 차량부터 순회
    for i in range(1, len(routes)):
        start, end = routes[i][0], routes[i][1]

        # 다음 차의 출발지점이 현재 카메라 기준점보다 뒤에 있다면 (새로운 카메라 필요)
        if start > now_camera_position:
            camera_count += 1
            now_camera_position = end  # 새 카메라를 이 차의 도착지점에 설치(초기 카메라 설치처럼)
        else:
            # 다음 차의 도착지점이 카메라 위치보다 더 앞이라면
            # 두 차를 모두 잡기 위해 카메라를 더 앞에 설치
            if end < now_camera_position:
                now_camera_position = end

    return camera_count