for t in range(int(input())):
    word = input()

    first_line = '..#.'
    second_line = '.#.#'
    third_line = '#.'
    third_line_2 = '.'

    print(first_line * len(word) + '.')
    print(second_line * len(word) + '.')
    for i in range(len(word)):
        print(third_line + word[i] +  third_line_2, end="")
        if i == len(word) - 1:
            print('#')
    print(second_line * len(word) + '.')
    print(first_line * len(word) + '.')