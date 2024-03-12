def solution(a, b):
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 1월 1일부터 a-1월 마지막 날까지의 일수를 구한다.
    sum = 0
    
    for i in range(a-1):
        sum += months[i]
        
    sum += b
    
    sum %= 7
    
    return days[sum-1]
