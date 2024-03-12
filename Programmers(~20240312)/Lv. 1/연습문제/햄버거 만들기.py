def solution(ingredients):
    # 햄버거를 만들 수 있는 패턴
    pattern = [1, 2, 3, 1]
    # 포장하는 햄버거의 개수
    hamburgers = 0
    
    stack = []
    
    for ingredient in ingredients:
        stack.append(ingredient)
        if len(stack) >= 4:
            if stack[-4:] == pattern:
                for _ in range(4):
                    stack.pop()
                hamburgers += 1
                
    return hamburgers