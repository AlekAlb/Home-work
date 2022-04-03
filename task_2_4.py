employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for person in employees:
    name = person.split()[-1].title()
    print(f'Привет, {name}!')