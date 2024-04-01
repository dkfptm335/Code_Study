# def is_palindrome(row):
#     if row == row[::-1]:
#         return True
#     return False
#
#
# def get_max_palindrome_length(row):
#     length = []
#
#     for i in range(len(row)):
#         for j in range(i + 1, len(row) + 1):
#             tmp = row[i:j]
#             if is_palindrome(tmp):
#                 length.append(len(tmp))
#
#     return max(length)
#
#
# for tc in range(1, 11):
#     testNum = int(input())
#     board = [list(input().strip()) for _ in range(100)]
#     board_transpose = list(zip(*board))
#     max_length = []
#
#     for line in board:
#         max_length.append(get_max_palindrome_length(line))
#
#     for line in board_transpose:
#         max_length.append(get_max_palindrome_length(line))
#
#     print(f"#{tc} {max(max_length)}")

# 위 코드는 정상적으로 실행 가능하지만, SWEA 채점 오류가 발생하기 때문에 다른 코드로 제출

for _ in range(10) :
    T = int(input())
    board = []
    for _ in range(100) :
        board.append(input())

    def check(string, length) :
        max = length
        while(length <= 100) :
            answer = 0
            for i in range(100) :
                for j in range(101-length) :
                    word = string[i][j:j+length]
                    if word == word[::-1] :
                        max = length
                        answer = 1
                        break
                if answer == 1 :
                    break
            length += 1
        return max

    # 가로줄
    row = check(board, 1)

    # 세로줄
    transposed_board = []
    for i in range(100) :
        list = ""
        for j in range(100) :
            list += board[j][i]
        transposed_board.append(list)

    col = check(transposed_board, 1)

    print("#{} {}".format(T, max(row, col)))
    # 출처: https://o-sae.tistory.com/36