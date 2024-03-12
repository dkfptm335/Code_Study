def solution(price, money, count):
    price_sum = 0
    
    for i in range(1, count + 1):
        price_sum += price * i
    
    if price_sum > money:
        return price_sum - money
    else:
        return 0
    