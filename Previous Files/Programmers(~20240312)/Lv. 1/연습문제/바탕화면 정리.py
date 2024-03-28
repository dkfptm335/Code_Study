def solution(wallpaper):
    # 파일의 위치를 기준으로 꼭짓점으로 확장하는 새 배열 생성
    new_wp = [[0] * (len(wallpaper[0])+1) for _ in range(len(wallpaper)+1)]
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                new_wp[i][j] = 1
                new_wp[i][j+1] = 1
                new_wp[i+1][j] = 1
                new_wp[i+1][j+1] = 1
                
    # 사각형 그리기
    # 1. 1이 존재하는 최상단의 행 찾기
    ur, uc, dr, dc = 0, 0, 0, 0
    for i in range(len(new_wp)):
        if 1 in new_wp[i]:
            ur = i
            break
            
    # 2. 1이 존재하는 최하단의 행 찾기
    for i in range(len(new_wp)-1, -1, -1):
        if 1 in new_wp[i]:
            dr = i
            break
            
    # 3. 1이 존재하는 첫 번째 열 찾기
    for i in range(len(new_wp[0])):
        for j in range(len(new_wp)):
            if new_wp[j][i] == 1:
                dc = i
                break
                
    for i in range(len(new_wp[0])-1, -1, -1):
        for j in range(len(new_wp)-1, -1, -1):
            if new_wp[j][i] == 1:
                uc = i
                break
                
    return [ur, uc, dr, dc]
