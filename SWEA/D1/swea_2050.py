alphabet_mapping = {chr(65+i):i+1 for i in range(26)}
str = input()
for i in range(len(str)):
    print(alphabet_mapping[str[i]], end=' ')