
#список предметов
stuffdict = {'винтовка': (3, 25, 'в'),
             'пистолет': (2, 15, 'п'),
             'боекомплект': (2, 15, 'б'),
             'аптечка': (2, 20, 'а'),
             'ингалятор': (1, 5, 'и'),
             'нож': (1, 15, 'н'),
             'топор': (3, 20, 'т'),
             'оберег': (1, 25, 'о'),
             'фляжка': (1, 15, 'ф'),
             'днтидот': (1, 10, 'а'),
             'еда': (2, 20, 'е'),
             'арбалет': (2, 20, 'р')}

# Вариант 5: ячейки 2х4, астма, 20 начальных очков
start_points = 20
space = 8
# увеличиваю количество очков ингалятора, чтобы алгоритм добавил его в рюкзак. при подсчете очков надбавку вычтем
stuffdict['ингалятор'] = (1, 5 + 100, 'и')


# списки свойств предметов
size = [stuffdict[items][0] for items in stuffdict]
points = [stuffdict[items][1] for items in stuffdict]
names = [stuffdict[items][2] for items in stuffdict]

#количество предметов
n = len(points)


# функция создает и заполняет таблицу мемоизации
def meme_table(stuffdict, space):

    T = [[0 for i in range(space + 1)] for j in range(n + 1)]

    for i in range(n+1):
        for s in range(space+1):
            if i == 0 or s == 0:
                T[i][s] = 0
            elif size[i - 1] <= s:
                T[i][s] = max(points[i - 1] + T[i - 1][s - size[i - 1]], T[i - 1][s])
            else:
                T[i][s] = T[i - 1][s]
    return T

T = meme_table(stuffdict, space)

# функция по данным из таблицы кладет вещи в рюкзак
def get_items(stuffdict):

    s = space
    i = n

    res = T[n][s]
    backpack = []
    r=1
    while res > 0 and i > 0:
        if res != T[i-1][s]:
            # кладем в рюкзак предмет, соответственно его размеру
            for r in range(size[i-1]):
                backpack.append(names[i-1])
            res -= points[i-1]
            s -= size[i-1]
        i -= 1

    # вычетаем очки предметов, которые в рюкзак не попали
    for i in range(n):
        if not(names[i] in backpack):
            T[n][space] -= points[i]

    # добавляем к результату алгоритма начальные очки и вычитаем 100, добавленные в начале
    T[n][space] += start_points - 100

    return backpack, T[n][space]

backpack, result = get_items(stuffdict)

i = 0
# вывод предметов в рюкзаке в виде таблицы 2х4
for name in backpack:
    print(f'[{name}]', end='')
    i += 1
    if i%4 == 0:
        print('')

print(result)