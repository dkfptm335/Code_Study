T = int(input())


for tc in range(1, T + 1):
    word = input()
    vowels = ['a', 'e', 'i', 'o', 'u']
    newWord = ''

    for char in word:
        if char not in vowels:
            newWord += char

    print(f"#{tc} {newWord}")
