s = " "
max_count = 0
for index,_ in enumerate(s):
    letters = []
    count = 0
    for letter in s[index:]:
        if letter in letters:
            if count > max_count:
                max_count = count
            count = 1
            letters = []
            letters.append(letter)
        else:
            count += 1
            letters.append(letter)
    if count > max_count:
        max_count = count
print(max_count)