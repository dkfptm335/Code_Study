def solution(k, score):
    answer = []
    rank = []
    
    for i in range(len(score)):
        if i <= k-1:
            rank.append(score[i])
            rank.sort(reverse=True)
            answer.append(rank[-1])
        else:
            if score[i] >= rank[-1]:
                rank.pop()
                rank.append(score[i])
                rank.sort(reverse=True)
                answer.append(rank[-1])
            else:
                answer.append(rank[-1])
        
    return answer
