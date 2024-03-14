# 영문 문장을 입력받아 모음의 개수를 세는 프로그램을 작성하시오. 모음은 'a', 'e', 'i', 'o', 'u'이며 대문자 또는 소문자이다.
from collections import Counter

def count_vowels(sentence):
    vowels = 'aeiou'
    sentence = sentence.lower()
    counter = Counter(sentence)
    result = 0
    for vowel in vowels:
        result += counter[vowel]
    return result

str_list = []

while True:
    str = input()
    if str == "#":
        break
    str_list.append(str)
    
for s in str_list:
    print(count_vowels(s))