def solution(my_string, indices):
    
    # string to list
    string_list = list(my_string)
    
    # indices에 들어있는 인덱스를 앞에서부터 제거하게 되면 그만큼 my_string에 변화가 생기기 때문에,
    # indices를 내림차순 정렬 후 뒤에서부터 제거한다.
    
    # indices 내림차순 정렬
    indices.sort()
    indices.reverse()
    
    for idx in indices:
        del string_list[idx]
    
    return ''.join(string_list)
