def solution(my_string, num1, num2):
    
    def swap(a, b):
        return b, a
    
    my_string = list(my_string)
    
    my_string[num1], my_string[num2] = swap(my_string[num1], my_string[num2])
    
    answer = ''.join(my_string)
    
    return answer
