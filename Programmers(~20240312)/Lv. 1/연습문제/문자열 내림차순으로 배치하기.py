def solution(s):
    list_str = list(s)
    list_str.sort(reverse=True)
    return ''.join(list_str)
