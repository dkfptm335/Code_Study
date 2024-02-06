def solution(polynomial):
    # + 기호를 기준으로 나누어 리스트에 저장
    polynomial = polynomial.split('+')
    
    for i in range(len(polynomial)):
        polynomial[i] = polynomial[i].strip()
        
    x_list = []
    num_list = []
    
    for poly in polynomial:
        if 'x' in poly:
            if poly[0] == 'x':
                x_list.append(1)
            elif poly[0] == '-':
                x_list.append(-1)
            else:
                x_list.append(int(poly[:-1]))
        else:
            num_list.append(int(poly))
    
    a = sum(x_list)
    b = sum(num_list)
    
    px = ''
    q = ''
    
    if a == 0:
        px = None
    elif a == 1:
        px = 'x'
    elif a == -1:
        px = '-x'
    else:
        px = str(a) + 'x'
    
    if b == 0:
        q = None
    else:
        q = str(b)
        
    if px == None and q == None:
        return '0'
    elif px == None:
        return q
    elif q == None:
        return px
    else:
        return px + ' + ' + q
    