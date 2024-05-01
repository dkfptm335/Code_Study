def isPalindrome(s):
    return s == s[::-1]


t = int(input().strip())
answers = []
for tc in range(t):
    target = input().strip()
    if "?" not in target:
        if isPalindrome(target):
            answers.append("Exist")
        else:
            answers.append("Not exist")
    else:
        target = list(target)
        for i in range(len(target)):
            if target[i] == "?":
                target[i] = target[len(target) - 1 - i]

        while "?" in target:
            target.remove("?")

        if isPalindrome(target):
            answers.append("Exist")
        else:
            answers.append("Not exist")

for i in range(len(answers)):
    print(f"#{i + 1} {answers[i]}")
