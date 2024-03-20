def is_palindrome(s):
    return s == s[::-1]


while True:
    number = input()
    if number == '0':
        break
    if is_palindrome(number):
        print('yes')
    else:
        print('no')
