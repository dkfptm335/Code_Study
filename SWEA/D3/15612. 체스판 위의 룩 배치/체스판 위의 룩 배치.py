t = int(input())

for tc in range(1, t + 1):
    chessBoard = [list(input()) for _ in range(8)]
    chessBoard_transpose = list(map(list, zip(*chessBoard)))
    rookCount = 0
    isPossible = True
    finalDecision = True

    # 룩 개수 세기
    for chess in chessBoard:
        for obj in chess:
            if obj == 'O':
                rookCount += 1

    for chess in chessBoard:
        if chess.count('O') != 1:
            isPossible = False

    for chess in chessBoard_transpose:
        if chess.count('O') != 1:
            isPossible = False

    if rookCount != 8 or isPossible == False:
        finalDecision = False

    print(f"#{tc} {'yes' if finalDecision else 'no'}")
    