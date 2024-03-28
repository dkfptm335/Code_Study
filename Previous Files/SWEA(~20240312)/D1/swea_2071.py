# 테스트 케이스의 개수 T
T = int(input())

means = []

# 테스트 케이스의 개수만큼 테스트 데이터 입력, 케이스 한개당 10개의 수를 이용하여 평균값을 구함
for i in range(T):
    # 각 줄에 10개의 수를 입력받아 리스트에 저장
    num_list = list(map(int, input().split()))
    sum = 0
    # 리스트의 합을 구함
    for j in range(len(num_list)):
        sum += num_list[j]
    mean = round(sum / 10.0)
    means.append(mean)

for i in range(len(means)):
    print('#' + str(i + 1) + ' ' + str(means[i]))