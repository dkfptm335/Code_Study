def solution(park, routes):
    # 장애물 좌표 저장할 리스트
    obstacles = []
    # 시작 지점 좌표
    x, y = 0, 0
    
    # 시작 지점과 장애물 좌표 구하기
    for i in range(len(park)):
        if 'S' in park[i] or 'X' in park[i]:
            for j in range(len(park[i])):
                if park[i][j] == 'S':
                    x, y = i, j
                elif park[i][j] == 'X':
                    obstacles.append((i, j))
                    
    for route in routes:
        direction, distance = route.split()
        # 이동 거리 형변환
        distance = int(distance)
        
        # 동쪽
        if direction == 'E':
            # 이동 거리만큼 이동했을 때 배열의 범위를 벗어나지 않는지 확인, 만약 벗어난다면 다음 루프로 넘어가기
            if y + distance >= len(park[0]):
                continue
                
            # 이동 거리만큼 이동했을 때 장애물이 있는지 확인
            for i in range(1, distance + 1):
                # 장애물이 있다면 다음 루프로 넘어가고, 없다면 이동거리만큼 이동
                if (x, y + i) in obstacles:
                    break
            else:
                y += distance
                
        # 서쪽
        elif direction == 'W':
            if y - distance < 0:
                continue
                
            for i in range(1, distance + 1):
                if (x, y - i) in obstacles:
                    break
            else:
                y -= distance
                
        # 남쪽
        elif direction == 'S':
            if x + distance >= len(park):
                continue
                
            for i in range(1, distance + 1):
                if (x + i, y) in obstacles:
                    break
            else:
                x += distance
                
        # 북쪽
        elif direction == 'N':
            if x - distance < 0:
                continue
                
            for i in range(1, distance + 1):
                if (x - i, y) in obstacles:
                    break
            else:
                x -= distance
                
    return [x, y]
