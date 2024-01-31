def solution(my_string, queries):
    
    for query in queries:
        my_string = my_string[:query[0]]+(my_string[query[0]:query[1]+1])[::-1]+my_string[query[1]+1:]
        
    return my_string
