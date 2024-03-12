def solution(score):
    # score = [[영어, 수학], [영어, 수학], ...]
    
    average = [sum(i) for i in score]
    
    sorted_average = sorted(average, reverse=True)
    
    ranks = [sorted_average.index(i) + 1 for i in average]
        
    return ranks
