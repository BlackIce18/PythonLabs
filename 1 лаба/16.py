'''
Напишите скрипт, который на основе списка из 16 названий
футбольных команд случайным образом формирует 4 группы по 4
команды, а также выводит на консоль календарь всех игр (игры
должны проходить по средам, раз в 2 недели, начиная с 14 сентября
текущего года). Даты игр необходимо выводить в формате «14/09/2016,
22:45». Используйте модули random и itertools.
'''
import random
import itertools
from datetime import datetime, timedelta

TeamList = [
    'Реал Мадрид',
    'Бавария',
    'Манчестер Юнайтед',
    'Барселона',
    'Индепендьенте',
    'Бока Хуниорс',
    'Сантос',
    'Ювентус',
    'Пеньяроль',
    'Ривер Плейт',
    'Фламенго',
    'Милан',
    'Ливерпуль',
    'Ботафого',
    'Бенфика',
    'Арсенал'
]

random.shuffle(TeamList)
print('Команды:')
print('\n'.join(TeamList))

print('---------------------------------------------')
TeamListGroup = [TeamList[i:i + 4] for i in range(0, len(TeamList), 4)]  # range(start, end, step)

mathes = []
format = "%d/%m/%Y, %H:%M"
startMatches = datetime.strptime("14/09/2016, 22:45", format)
for t in TeamListGroup:
    mathes.append([c for c in itertools.combinations(t, 2)])

print('Жеребьевка')
for i in range(0, 6):
        print("Группа: ", i+1)
        print(mathes[0][i], mathes[1][i], mathes[2][i], mathes[3][i], sep="\n")
        print('Расписание матчей')
        print(startMatches.strftime(format))
        startMatches = startMatches + timedelta(days=14)


'''
# -------date----------
tempDate = "14.09.2020"
startTime = [14, 9, 2020]
endTime = [31, 3, 2021]

print('Сезон начинается в', str(startTime[0]) + '/' + str(startTime[1]) + '/' + str(startTime[2]) + ' ' + str('22:45'))
print('Сезон заканчивается в', str(endTime[0]) + '/' + str(endTime[1]) + '/' + str(endTime[2]) + ' ' + str('22:45'))
now_date = datetime.now()
now_date = now_date.replace(2020, 9, 14)
print('\n')

# ---------------------
a = datetime(2020, 9, 14)
b = timedelta(days=14)
i = 0

print('%s/%s/%s' % (a.day, a.month, a.year) + '   22:45  ' + str(TeamList[i]) + '  &  ' + str(TeamList[i + 1]))
i += 1
a = datetime(2020, 9, 16)

while a <= datetime(2021, 3, 31):  # season end
    a = a + b  # + 14 days
    if (i < 15):
        print('%s/%s/%s' % (a.day, a.month, a.year) + '   22:45  ' + str(TeamList[i]) + '  &  ' + str(TeamList[i + 1]))
        i += 1
    else:
        print('%s/%s/%s' % (a.day, a.month, a.year) + '   22:45  ' + str(TeamList[15]) + '  &  ' + str(TeamList[0]))
        break
'''