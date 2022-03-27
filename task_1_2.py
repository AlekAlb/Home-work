numbers_1 = []
numbers_2 = []
numbers_3 = []
sum_2 = 0
sum_3 = 0
for number in range(1, 1001):
    if number % 2 != 0:
        numbers_1.append(number**3)
#print(numbers_1)
for number in numbers_1:
    number1 = number
    a = []
    while number != 0:
        a.append(number % 10)
        number = number // 10
    sum_1 = 0
    for i in a:
        sum_1 += i
    if sum_1 % 7 == 0:
        sum_2 += number1
        numbers_2.append(number1)
print(sum_2)
#print(numbers_2)
for number in numbers_1:
    numbers_3.append(number + 17)
#print(numbers_3)
for number in numbers_3:
    number1 = number
    a = []
    while number != 0:
        a.append(number % 10)
        number = number // 10
    sum_1 = 0
    for i in a:
        sum_1 += i
    if sum_1 % 7 == 0:
        sum_3 += number1
print(sum_3)