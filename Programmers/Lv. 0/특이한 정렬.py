def swap(a, b):
    return b, a

def solution(numlist, n):
    for i in range(len(numlist)):
        for j in range(i, len(numlist)):
            if abs(numlist[i]-n) > abs(numlist[j]-n):
                numlist[i], numlist[j] = swap(numlist[i], numlist[j])
            elif abs(numlist[i]-n) == abs(numlist[j]-n):
                if numlist[i] < numlist[j]:
                    numlist[i], numlist[j] = swap(numlist[i], numlist[j])
                    
    return numlist
