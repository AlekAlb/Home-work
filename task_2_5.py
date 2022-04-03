prices_of_goods = [69.99, 43.4, 56.5, 60, 64.3, 68.4, 90, 95.9, 13.1, 15.66, 95.56, 50.34, 20]
price_rub = []
price_kop = []
price_rub_kop = []
for price in prices_of_goods:
    price_str = str(price)
    price_apart = price_str.split('.')
    price_rub = price_apart[0] + ' руб'
    if price_str.find('.') != -1 and int(price_apart[1]) >= 10:
        price_kop = price_apart[-1] + ' коп'
    elif price_str.find('.') != -1:
        price_kop = price_apart[1] + '0 коп'
    else:
        price_kop = '00 коп'
    price_rub = price_rub + ' ' + price_kop
    price_rub_kop.append(price_rub)
print(id(price_rub_kop), price_rub_kop)
price_rub_kop.sort()
print(id(price_rub_kop), price_rub_kop)
"""
Объект списка после сортировки остался тот же самый, т.к. id одинаковое.
"""
print(list(reversed(price_rub_kop))[:5])
