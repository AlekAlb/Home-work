list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list2 = []
for elem in list1:
    elem_last = elem[-1]
    if elem_last.isdigit() == True:
        list3 = []
        list2.append('"')
        if elem.isdigit() == True and len(elem) != 1:
            list2.append(elem)
            list2.append('"')
        elif elem.isdigit() == True and len(elem) == 1:
            elem = f'0{elem}'
            list2.append(elem)
            list2.append('"')
        elif len(elem) == 2 and elem.find('+') != -1 or elem.find('-') != -1:
            list3.append(elem[0])
            list3.append('0')
            list3.append(elem[1])
            a = ''.join(list3)
            list2.append(a)
            list2.append('"')
        else:
            list2.append(elem)
    else:
        list2.append(elem)
list4 = []
for k in range(len(list2)):
    if list2[k] == '"' and list2[k+1][-1].isdigit() == True and list2[k+2] == '"':
        list3 = []
        list3.append(list2[k])
        list3.append(list2[k+1])
        list3.append(list2[k+2])
        a = ''.join(list3)
        list4.append(a)
    elif list2[k][-1].isdigit() == False and list2[k] != '"':
        list4.append(list2[k])
print(list1)
print(list2)
print(' '.join(list4))