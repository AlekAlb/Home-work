word = 'процент'
for i in range(1, 101):
    if i == 1 or (i > 20 and i % 10 == 1):
        print(i, word)
    elif i >= 2 and i<= 4 or (i > 21 and (i % 10 == 2 or i % 10 == 3 or i % 10 == 4)):
        print(i, word + 'а')
    else:
        print(i, word + 'ов')