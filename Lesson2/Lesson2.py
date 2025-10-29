# 1 Квадрат
storona = 10

per = storona * 4
plosh = storona * storona
diag = storona * (2 ** 0.5)

print(per, plosh, diag)


# 2 Квадратное уравнение
a = 1
b = 4
c = 3

disk = (b ** 2) - (4 * a * c)
koren1 = (disk ** 0.5 - b) / (2 * a)
koren2 = (- (disk ** 0.5) + b) / (2 * a)

print(disk, round(koren1, 2), round(koren2, 2))


# 3 Две строки
str1 = 'абвг'
str2 = 'дежзи'
zam = str1.replace(str1[0] + str1[1], str2[0] + str2[1]) + ' ' + str2.replace(str2[0] + str2[1], str1[0] + str1[1])

print(zam)


# 4 Путь до файла
putt = 'C:\\Users\\dv.eremin\\Downloads\\clip0096.avi'
putt2 = putt.split('\\')
filename = putt2[-1].split('.')

print('имя файла ' + filename[-2], 'корневая папка ' + putt2[1])


# 5 2 числа
a1 = 2
a2 = 3

print('%s + %s = %s' % (a1, a2, (a1 + a2)))
print('{}*{} = {}'.format(a1, a2, a1 * a2))


# 6 удаление символов
str3 = 'строка текста проверка пробелов'

print(str3[0::2])


# 7 2 строки
str71 = 'абв'
str72 = 'гдеаж зиквлм нопрсбтд'
poz = (str72.find(str71[0]), str72.find(str71[1]), str72.find(str71[2]))
poz_min = min(poz)
poz_max = max(poz) + 1

print(str72[poz_min:poz_max])
