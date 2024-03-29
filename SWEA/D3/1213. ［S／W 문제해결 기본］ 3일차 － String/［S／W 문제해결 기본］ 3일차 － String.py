for tc in range(1, 11):
    testNum = int(input())
    word = input()
    sentence = input()

    print(f"#{tc} {sentence.count(word)}")