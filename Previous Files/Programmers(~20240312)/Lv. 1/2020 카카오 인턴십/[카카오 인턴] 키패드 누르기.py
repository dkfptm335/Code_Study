# 두 키 사이의 거리를 반환하는 함수
def get_distance(key1, key2):
    keypad = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#']
    ]

    key1_x, key1_y = 0, 0
    key2_x, key2_y = 0, 0
    
    for i in range(len(keypad)):
        for j in range(len(keypad[i])):
            if keypad[i][j] == key1:
                key1_x, key1_y = i, j
            if keypad[i][j] == key2:
                key2_x, key2_y = i, j
                
    return abs(key1_x - key2_x) + abs(key1_y - key2_y)
    
def solution(numbers, hand):
    result = ''
    # 초기 왼손 엄지손가락과 오른손 엄지손가락의 위치
    left = ['*']
    right = ['#']
    
    for num in numbers:
        # 왼손 엄지손가락을 사용하는 경우
        if num == 1 or num == 4 or num == 7:
            result += 'L'
            left.append(str(num))
        # 오른손 엄지손가락을 사용하는 경우
        elif num == 3 or num == 6 or num == 9:
            result += 'R'
            right.append(str(num))
        # 가운데 숫자를 사용하는 경우
        else:
            # 각각의 숫자와 왼손, 오른손 엄지손가락 사이의 거리를 구함
            l_dist = get_distance(left[-1], str(num))
            r_dist = get_distance(right[-1], str(num))
            
            # 왼손 엄지손가락과 오른손 엄지손가락 사이의 거리를 비교하여 가까운 쪽의 엄지손가락을 사용
            if l_dist < r_dist:
                result += 'L'
                left.append(str(num))
            elif l_dist > r_dist:
                result += 'R'
                right.append(str(num))
            # 거리가 같은 경우
            else:
                # 왼손잡이인 경우
                if hand == 'left':
                    result += 'L'
                    left.append(str(num))
                # 오른손잡이인 경우
                else:
                    result += 'R'
                    right.append(str(num))
                    
    return result
