music = 'cdefgabC'
music_dict = {}

for idx, value in enumerate(music):
    music_dict[idx + 1] = value

music_number = input()

sentence = ''

for number in music_number.split():
    sentence += music_dict[int(number)]

if sentence == music:
    print('ascending')
elif sentence == music[::-1]:
    print('descending')
else:
    print('mixed')