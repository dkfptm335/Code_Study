T = int(input())
test_cases = {}
 
for i in range(1, T+1):
    N, K = map(int, input().split())
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    students = []
    scores = []
 
    for j in range(1, N+1):
        mid, final, test = map(int, input().split())
        students.append([j, mid*0.35 + final*0.45 + test*0.2])
 
    students.sort(key=lambda x: x[1], reverse=True)
    # 등급 부여 한도: N // 10
    pos = 0
    for grade in grades:
        for j in range(N//10):
            students[pos][1] = grade
            pos += 1
 
    students = {idx: grade for idx, grade in students}
    test_cases[i] = students[K]
 
for key, value in test_cases.items():
    print(f'#{key} {value}')