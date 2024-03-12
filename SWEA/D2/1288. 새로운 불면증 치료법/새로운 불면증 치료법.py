T = int(input())
test_case = {i+1: 0 for i in range(T)}

for t in range(T):
    N = int(input())
    num_dict = {str(i): False for i in range(10)}
    
    while not all(num_dict.values()):
        test_case[t+1] += N
        for n in str(test_case[t+1]):
            num_dict[n] = True
        
for t in range(T):
    print(f'#{t+1} {test_case[t+1]}')
    