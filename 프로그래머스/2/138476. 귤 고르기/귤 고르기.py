from collections import Counter

def solution(k, tangerine):
    cnt = Counter(tangerine)
    cnt = cnt.most_common(len(cnt))
    
    variation = 0
    count = 0
    
    for i in range(len(cnt)):
        count += cnt[i][1]
        variation += 1
        
        if count >= k:
            break
            
    return variation