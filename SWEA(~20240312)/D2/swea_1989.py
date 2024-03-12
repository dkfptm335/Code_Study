# 초심자의 회문 검사
# 회문이란? 121, 12421과 같이 앞으로 읽으나 뒤로 읽으나 같은 문자열을 말한다. (palindrome)

# 팰린드롬 검사 함수
def is_palindrome(str):
    if str == str[::-1]:
        return 1
    return 0

# 테스트 케이스 T
T = int(input())

answer = []

for i in range(T):
    str = input()
    answer.append(is_palindrome(str))

for i in range(T):
    print(f'#{i+1} {answer[i]}')