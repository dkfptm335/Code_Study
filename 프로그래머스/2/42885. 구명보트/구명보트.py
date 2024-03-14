from collections import deque

def solution(people, limit):
    # 구명보트는 한 번에 최대 2명
    # 무게 제한
    
    # 가설 1: 가장 무거운 사람과 가장 가벼운 사람을 태운다?
    boat = 0
    people.sort()
    people = deque(people)
    
    while people:
        if people[-1] + people[0] <= limit and len(people) >= 2:
            people.popleft()
            people.pop()
            boat += 1
        else:
            people.pop()
            boat += 1
            
    return boat