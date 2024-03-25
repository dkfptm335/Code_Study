import sys
from collections import deque


sentences = []
while True:
    sentence = input()
    if sentence == ".":
        break
    sentences.append(sentence)

test_cases = {i: 'yes' for i in range(len(sentences))}

for sentence in sentences:
    tmp = ''
    for char in sentence:
        if char not in ['(', ')', '[', ']', '.', ' ']:
            continue
        tmp += char

    while " " in tmp:
        tmp = tmp.replace(" ", "")
    while "." in tmp:
        tmp = tmp.replace(".", "")

    deq = deque(list(tmp))
    stack = []

    while deq:
        if not stack:
            stack.append(deq.popleft())
        else:
            if stack[-1] == "(" and deq[0] == ")":
                stack.pop()
                deq.popleft()
            elif stack[-1] == "[" and deq[0] == "]":
                stack.pop()
                deq.popleft()
            else:
                stack.append(deq.popleft())

    if stack:
        test_cases[sentences.index(sentence)] = 'no'

for key, value in test_cases.items():
    print(value)