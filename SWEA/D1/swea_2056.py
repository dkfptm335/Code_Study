T  = int(input()) # 테스트 케이스 개수
date = []

for i in range(T):
    date.append(input())
    
for i in range(T):
    year = int(date[i][0:4])
    month = int(date[i][4:6])
    day = int(date[i][6:8])
    
    if 1 <= month <= 12:
        if month == 1 | month == 3 | month == 5 | month == 7 | month == 8 | month == 10 | month == 12:
            if 1 <= day <= 31:
                print(f'#{i+1} {year:04}/{month:02}/{day:02}')
            else:
                print(f'#{i+1} -1')
        elif month == 4 | month == 6 | month == 9 | month == 11:
            if 1 <= day <= 30:
                print(f'#{i+1} {year:04}/{month:02}/{day:02}')
            else:
                print(f'#{i+1} -1')
        else:
            if 1 <= day <= 28:
                print(f'#{i+1} {year:04}/{month:02}/{day:02}')
            else:
                print(f'#{i+1} -1')
    else:
        print(f'#{i+1} -1')