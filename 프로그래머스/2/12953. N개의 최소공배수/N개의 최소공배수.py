def solution(arr):
    lcm = arr[-1]
    
    while True:
        count = 0
        for num in arr:
            if lcm % num == 0:
                count += 1
        
        if count == len(arr):
            break
        else:
            lcm += arr[-1]
            
    return lcm