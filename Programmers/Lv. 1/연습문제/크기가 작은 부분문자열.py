def get_part_string(str, length):
    part_string = []
    
    for i in range(0, len(str)-length+1):
        part_string.append(str[i:i+length])
    
    return part_string

def solution(t, p):
    count = 0
    
    for val in get_part_string(t, len(p)):
        if int(val) <= int(p):
            count += 1
            
    return count
