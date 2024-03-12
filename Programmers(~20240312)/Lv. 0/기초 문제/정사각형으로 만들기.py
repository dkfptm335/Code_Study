# 문제 설명
# 이차원 정수 배열 arr이 매개변수로 주어집니다.
# arr의 행의 수가 더 많다면 열의 수가 행의 수와 같아지도록 각 행의 끝에 0을 추가하고,
# 열의 수가 더 많다면 행의 수가 열의 수와 같아지도록 각 열의 끝에 0을 추가한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.

def solution(arr):
    
    rows = len(arr)
    cols = len(arr[0])
    
    if rows > cols:
        for i in range(rows):
            for j in range(rows - cols):
                arr[i].append(0)
    
    elif rows < cols:
        for i in range(cols - rows):
            arr.append([0] * cols)

    else:
        pass
    
    return arr
