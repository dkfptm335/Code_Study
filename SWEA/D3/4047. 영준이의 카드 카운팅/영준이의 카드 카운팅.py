t = int(input())

for tc in range(1, t + 1):
    cards = list(input())
    cardDict = {
        'S': [0] * 13,
        'D': [0] * 13,
        'H': [0] * 13,
        'C': [0] * 13
    }
    parsedCards = []
    tmp = []
    for char in cards:
        if not tmp:
            tmp.append(char)
        else:
            if char.isalpha():
                parsedCards.append(tmp)
                tmp = [char]
            else:
                tmp.append(char)
    parsedCards.append(tmp)

    for card in parsedCards:
        cat = card[0]
        number = int(f"{card[1]}{card[2]}")
        cardDict[cat][number - 1] += 1

    isPossible = True
    for idx, value in cardDict.items():
        for val in value:
            if val > 1:
                isPossible = False
                break

    cardDemand = list()
    if isPossible:
        for idx, value in cardDict.items():
            cardDemand.append(value.count(0))

    if isPossible:
        print(f"#{tc} {' '.join(list(map(str, cardDemand)))}")
    else:
        print(f"#{tc} ERROR")
        