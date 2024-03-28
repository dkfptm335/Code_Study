def solution(a, b, c, d):
    # 주사위 수를 저장할 리스트
    dice = [a, b, c, d]
    
    # 조건 1, 네 주사위의 값이 `p`로 모두 같을 때, `pppp`
    if len(set(dice)) == 1:
        return 1111 * a
    
    # 조건 2. 세 주사위의 값이 `p`, 나머지 하나가 `q`, `pppq`
    elif a==b and b==c and c!=d: return (10 * a + d)**2
    elif a==b and b==d and d!=c: return (10 * a + c)**2
    elif a==c and c==d and d!=b: return (10 * a + b)**2
    elif b==c and c==d and d!=a: return (10 * b + a)**2

    # 조건 3. 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 `p, q`, `ppqq`
    elif a==b and b!=c and c==d: return (a + d) * abs(a - d)
    elif a==c and c!=b and b==d: return (a + d) * abs(a - d)
    elif a==d and d!=b and b==c: return (a + c) * abs(a - c)

    # 조건 4. 어느 두 주사위에서 나온 숫자가 `p`로 같고 나머지 두 주사위에서 나온 숫자가 각각 `p`와 다른 `q, r(q ≠ r)`, `ppqr`
    elif a==b and a!=c and a!=d and c!=d: return c * d
    elif a==c and a!=b and a!=d and b!=d: return b * d
    elif a==d and a!=b and a!=c and b!=c: return b * c
    elif b==c and b!=a and b!=d and a!=d: return a * d
    elif b==d and b!=a and b!=c and a!=d: return a * c
    elif c==d and c!=a and c!=b and a!=b: return a * b

    # 조건 5. 네 주사위에 적힌 숫자가 모두 다르다면, `pqrs`
    if len(set(dice)) == 4:
        return min(dice)
