T = int(input())

for tc in range(1, T + 1):
    student = int(input())  # 학생의 수
    groupCount = student // 3  # 그룹의 수

    print(f"#{tc} {groupCount}")