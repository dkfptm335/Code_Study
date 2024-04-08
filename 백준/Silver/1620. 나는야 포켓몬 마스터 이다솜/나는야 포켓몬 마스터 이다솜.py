import sys
from collections import deque


N, M = map(int, sys.stdin.readline().strip().split())
number_pokemon = {i: sys.stdin.readline().strip() for i in range(1, N + 1)}
pokemon_number = {v: k for k, v in number_pokemon.items()}

questions = [sys.stdin.readline().strip() for _ in range(M)]
answers = []

for question in questions:
    if question.isdigit():
        answers.append(number_pokemon[int(question)])
    else:
        answers.append(pokemon_number[question])

for answer in answers:
    print(answer)
